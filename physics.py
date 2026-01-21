import sys
import math
import random
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from PyQt5.QtCore import QTimer, Qt
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluSphere, gluCylinder, gluQuadricDrawStyle, GLU_FILL, gluQuadricNormals, gluDisk, GLU_SMOOTH

class PhysicsObject:
    def __init__(self, x=0.0, y=0.0, z=0.0, half_dims=(0.5, 0.5, 0.5), color=(1.0, 0.0, 0.0), shape='sphere'):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z
        self.half_dims = half_dims
        self.color = color
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.shape = shape
        self.bounding_radius = math.sqrt(sum(d**2 for d in half_dims))
        hx, hy, hz = half_dims
        self.volume = 0.0
        if shape == 'sphere':
            self.volume = (4/3) * math.pi * hx**3
        elif shape in ['box', 'tall_box', 'wide_panel', 'thin_wall', 'floor_plate']:
            self.volume = 8 * hx * hy * hz
        elif shape in ['cylinder_v', 'cylinder_h', 'disc']:
            r = hx if shape == 'cylinder_v' or shape == 'disc' else hy
            h = 2 * (hy if shape == 'cylinder_v' or shape == 'disc' else hx)
            self.volume = math.pi * r**2 * h
        elif shape == 'cone':
            self.volume = (1/3) * math.pi * hx**2 * (2 * hy)
        elif shape in ['pyramid', 'octahedron']:
            self.volume = 8 * hx * hy * hz
        self.mass = self.volume if self.volume > 0 else 1.0

class PhysicsSim(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Physics Simulation (13 Complex Objects)")
        self.setMinimumSize(700, 700)
        self.GRAVITY = -9.81 * 0.01
        self.DAMPING = 0.90
        self.ROOM_SIZE = 12.0
        self.BOUNDARY = self.ROOM_SIZE / 2.0
        self.camera_x = 0.0
        self.camera_y = 0.0
        self.camera_z = self.ROOM_SIZE * 1.5
        self.camera_target = (0.0, 0.0, 0.0)
        self.objects = []
        self._initialize_objects()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(10)
        self.quadric = None

    def _initialize_objects(self):
        def get_safe_pos(dims):
            safe_range = self.BOUNDARY - max(dims) - 0.1
            return (random.uniform(-safe_range, safe_range),
                    random.uniform(-safe_range, safe_range),
                    random.uniform(-safe_range, safe_range))

        def get_random_vel(scale=0.5):
            return random.uniform(-scale, scale)

        self.objects.append(PhysicsObject(x=2.0, y=3.0, z=0.0, half_dims=(0.8, 0.8, 0.8), color=(1.0, 0.0, 0.0), shape='sphere'))
        self.objects[-1].vx = 0.5; self.objects[-1].vy = 0.5; self.objects[-1].vz = 0.5
        self.objects.append(PhysicsObject(x=-2.0, y=-3.0, z=0.0, half_dims=(0.6, 0.6, 0.6), color=(0.0, 0.0, 1.0), shape='sphere'))
        self.objects[-1].vx = -0.6; self.objects[-1].vy = 0.3; self.objects[-1].vz = 0.7
        self.objects.append(PhysicsObject(x=0.0, y=0.0, z=3.0, half_dims=(0.4, 0.4, 0.4), color=(0.0, 1.0, 0.0), shape='sphere'))
        self.objects[-1].vx = 0.8; self.objects[-1].vy = -0.4; self.objects[-1].vz = 0.1
        
        shape_definitions = [
            {'shape': 'box', 'dims': (0.6, 0.6, 0.6), 'color': (1.0, 0.5, 0.0)},
            {'shape': 'tall_box', 'dims': (0.3, 1.5, 0.3), 'color': (0.8, 0.2, 0.8)},
            {'shape': 'wide_panel', 'dims': (2.0, 0.2, 0.5), 'color': (0.2, 0.8, 0.8)},
            {'shape': 'thin_wall', 'dims': (0.1, 2.0, 1.5), 'color': (0.5, 0.5, 0.5)},
            {'shape': 'cylinder_v', 'dims': (0.7, 1.2, 0.7), 'color': (0.7, 0.7, 0.2)},
            {'shape': 'cylinder_h', 'dims': (1.2, 0.7, 0.7), 'color': (1.0, 0.2, 0.2)},
            {'shape': 'cone', 'dims': (0.8, 1.0, 0.8), 'color': (0.0, 0.5, 1.0)},
            {'shape': 'pyramid', 'dims': (1.0, 1.0, 1.0), 'color': (0.5, 0.0, 0.5)},
            {'shape': 'octahedron', 'dims': (0.7, 0.7, 0.7), 'color': (0.0, 1.0, 0.5)},
            {'shape': 'disc', 'dims': (1.5, 0.1, 1.5), 'color': (0.9, 0.9, 0.9)},
        ]

        for def_data in shape_definitions:
            dims = def_data['dims']
            pos = get_safe_pos(dims)
            obj = PhysicsObject(
                x=pos[0], y=pos[1], z=pos[2],
                half_dims=dims,
                color=def_data['color'],
                shape=def_data['shape']
            )
            obj.vx = get_random_vel(0.6)
            obj.vy = get_random_vel(0.6)
            obj.vz = get_random_vel(0.6)
            self.objects.append(obj)
    
    def initializeGL(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glShadeModel(GL_SMOOTH)
        glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 10.0, 10.0, 0.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        self.quadric = gluNewQuadric()
        gluQuadricDrawStyle(self.quadric, GLU_FILL)
        gluQuadricNormals(self.quadric, GLU_SMOOTH)

    def resizeGL(self, w, h):
        if h == 0:
            h = 1
        glViewport(0, 0, w, h)
        self._update_projection(w / h)

    def _update_projection(self, aspect_ratio):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, aspect_ratio, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(
            self.camera_x, self.camera_y, self.camera_z,
            self.camera_target[0], self.camera_target[1], self.camera_target[2],
            0.0, 1.0, 0.0
        )
        self._draw_room()
        for obj in self.objects:
            self._draw_object(obj)
            
    def _draw_room(self):
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        half = self.BOUNDARY
        glBegin(GL_QUADS)
        glColor4f(0.2, 0.2, 0.2, 0.7)
        glVertex3f(-half, -half, -half); glVertex3f( half, -half, -half)
        glVertex3f( half, -half,  half); glVertex3f(-half, -half,  half)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(0.1, 0.1, 0.1, 0.5)
        glVertex3f(-half, -half, -half); glVertex3f( half, -half, -half)
        glVertex3f( half,  half, -half); glVertex3f(-half,  half, -half)
        glEnd()
        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)
        
    def _set_material(self, color):
        mat_ambient = list(color) + [1.0]
        mat_diffuse = list(color) + [1.0]
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, mat_ambient)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, mat_diffuse)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.8, 0.8, 0.8, 1.0])
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 60.0)

    def _draw_object(self, obj):
        if not self.quadric: return
        glPushMatrix()
        self._set_material(obj.color)
        glTranslatef(obj.x_pos, obj.y_pos, obj.z_pos)
        hx, hy, hz = obj.half_dims
        if obj.shape == 'sphere':
            gluSphere(self.quadric, hx, 20, 20)
        elif obj.shape in ['box', 'tall_box', 'wide_panel', 'thin_wall', 'floor_plate']:
            self._draw_box(hx, hy, hz)
        elif obj.shape == 'cylinder_v' or obj.shape == 'disc':
            self._draw_cylinder(hx, 2 * hy)
        elif obj.shape == 'cylinder_h':
            glRotatef(90.0, 0.0, 0.0, 1.0)
            self._draw_cylinder(hy, 2 * hx)
        elif obj.shape == 'cone':
            glRotatef(-90.0, 1.0, 0.0, 0.0)
            glTranslatef(0.0, 0.0, -hy)
            gluCylinder(self.quadric, hx, 0.0, 2 * hy, 20, 20)
            self._draw_disk(hx, hy)
        elif obj.shape == 'pyramid':
            self._draw_pyramid(hx, hy, hz)
        elif obj.shape == 'octahedron':
            self._draw_octahedron(hx, hy, hz)
        glPopMatrix()

    def _draw_cylinder(self, radius, height):
        glRotatef(-90.0, 1.0, 0.0, 0.0)
        glTranslatef(0.0, 0.0, -height / 2.0)
        gluCylinder(self.quadric, radius, radius, height, 20, 20)
        glPushMatrix()
        gluDisk(self.quadric, 0.0, radius, 20, 1)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0.0, 0.0, height)
        gluDisk(self.quadric, 0.0, radius, 20, 1)
        glPopMatrix()
        
    def _draw_disk(self, radius, offset_y):
        glPushMatrix()
        glRotatef(90.0, 1.0, 0.0, 0.0)
        glTranslatef(0.0, 0.0, offset_y)
        gluDisk(self.quadric, 0.0, radius, 20, 1)
        glPopMatrix()
        
    def _draw_box(self, hx, hy, hz):
        s = 1.0
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0); glVertex3f(-hx, -hy, hz); glVertex3f( hx, -hy, hz)
        glVertex3f( hx,  hy, hz); glVertex3f(-hx,  hy, hz)
        glNormal3f(0.0, 0.0, -1.0); glVertex3f(-hx, -hy, -hz); glVertex3f(-hx,  hy, -hz)
        glVertex3f( hx,  hy, -hz); glVertex3f( hx, -hy, -hz)
        glNormal3f(0.0, 1.0, 0.0); glVertex3f(-hx, hy, -hz); glVertex3f(-hx, hy, hz)
        glVertex3f( hx, hy, hz); glVertex3f( hx, hy, -hz)
        glNormal3f(0.0, -1.0, 0.0); glVertex3f(-hx, -hy, -hz); glVertex3f( hx, -hy, -hz)
        glVertex3f( hx, -hy, hz); glVertex3f(-hx, -hy, hz)
        glNormal3f(1.0, 0.0, 0.0); glVertex3f( hx, -hy, -hz); glVertex3f( hx, hy, -hz)
        glVertex3f( hx, hy, hz); glVertex3f( hx, -hy, hz)
        glNormal3f(-1.0, 0.0, 0.0); glVertex3f(-hx, -hy, -hz); glVertex3f(-hx, -hy, hz)
        glVertex3f(-hx, hy, hz); glVertex3f(-hx, hy, -hz)
        glEnd()
    def _draw_pyramid(self, hx, hy, hz):
        glBegin(GL_QUADS)
        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(-hx, -hy, -hz); glVertex3f(hx, -hy, -hz); glVertex3f(hx, -hy, hz); glVertex3f(-hx, -hy, hz)
        glEnd()
        glBegin(GL_TRIANGLES)
        apex = (0.0, hy, 0.0)
        glNormal3f(0.0, hy, hz)
        glVertex3f(apex[0], apex[1], apex[2])
        glVertex3f(hx, -hy, hz); glVertex3f(-hx, -hy, hz)
        glNormal3f(hx, hy, 0.0)
        glVertex3f(apex[0], apex[1], apex[2])
        glVertex3f(hx, -hy, -hz); glVertex3f(hx, -hy, hz)
        glNormal3f(0.0, hy, -hz)
        glVertex3f(apex[0], apex[1], apex[2])
        glVertex3f(-hx, -hy, -hz); glVertex3f(hx, -hy, -hz)
        glNormal3f(-hx, hy, 0.0)
        glVertex3f(apex[0], apex[1], apex[2])
        glVertex3f(-hx, -hy, hz); glVertex3f(-hx, -hy, -hz)
        glEnd()
    def _draw_octahedron(self, hx, hy, hz):
        v = [
            ( 0.0,  hy,  0.0),
            ( 0.0, -hy,  0.0),
            ( hx,  0.0,  0.0),
            (-hx,  0.0,  0.0),
            ( 0.0,  0.0,  hz),
            ( 0.0,  0.0, -hz),
        ]
        def normal(v1, v2, v3):
            vx1, vy1, vz1 = v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]
            vx2, vy2, vz2 = v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]
            nx = vy1 * vz2 - vz1 * vy2
            ny = vz1 * vx2 - vx1 * vz2
            nz = vx1 * vy2 - vy1 * vx2
            mag = math.sqrt(nx*nx + ny*ny + nz*nz)
            return (nx/mag, ny/mag, nz/mag) if mag != 0 else (0.0, 0.0, 0.0)
        faces = [
            (0, 4, 2), (0, 2, 5), (0, 5, 3), (0, 3, 4),
            (1, 2, 4), (1, 5, 2), (1, 3, 5), (1, 4, 3)
        ]
        glBegin(GL_TRIANGLES)
        for i, j, k in faces:
            n = normal(v[i], v[j], v[k])
            glNormal3f(*n)
            glVertex3f(*v[i]); glVertex3f(*v[j]); glVertex3f(*v[k])
        glEnd()
    def keyPressEvent(self, event):
        thrust = 0.5
        obj = self.objects[0]
        if event.key() == Qt.Key_A or event.key() == Qt.Key_Left: obj.vx -= thrust
        elif event.key() == Qt.Key_D or event.key() == Qt.Key_Right: obj.vx += thrust
        elif event.key() == Qt.Key_Space: obj.vy += thrust * 5
        elif event.key() == Qt.Key_W or event.key() == Qt.Key_Up: obj.vz -= thrust
        elif event.key() == Qt.Key_S or event.key() == Qt.Key_Down: obj.vz += thrust
        super().keyPressEvent(event)
    def animate(self):
        self.update_physics()
        self.update()
    def update_physics(self):
        for i, obj1 in enumerate(self.objects):
            obj1.vy += self.GRAVITY
            obj1.x_pos += obj1.vx
            obj1.y_pos += obj1.vy
            obj1.z_pos += obj1.vz
            hx, hy, hz = obj1.half_dims
            if obj1.x_pos + hx > self.BOUNDARY:
                obj1.x_pos = self.BOUNDARY - hx
                obj1.vx *= -self.DAMPING
            if obj1.x_pos - hx < -self.BOUNDARY:
                obj1.x_pos = -self.BOUNDARY + hx
                obj1.vx *= -self.DAMPING
            if obj1.y_pos + hy > self.BOUNDARY:
                obj1.y_pos = self.BOUNDARY - hy
                obj1.vy *= -self.DAMPING
            if obj1.y_pos - hy < -self.BOUNDARY:
                obj1.y_pos = -self.BOUNDARY + hy
                obj1.vy *= -self.DAMPING
            if obj1.z_pos + hz > self.BOUNDARY:
                obj1.z_pos = self.BOUNDARY - hz
                obj1.vz *= -self.DAMPING
            if obj1.z_pos - hz < -self.BOUNDARY:
                obj1.z_pos = -self.BOUNDARY + hz
                obj1.vz *= -self.DAMPING
            r1 = obj1.bounding_radius
            for j in range(i + 1, len(self.objects)):
                obj2 = self.objects[j]
                r2 = obj2.bounding_radius
                dx = obj2.x_pos - obj1.x_pos
                dy = obj2.y_pos - obj1.y_pos
                dz = obj2.z_pos - obj1.z_pos
                distance = math.sqrt(dx*dx + dy*dy + dz*dz)
                min_distance = r1 + r2
                if distance < min_distance:
                    overlap = min_distance - distance
                    if distance != 0:
                        nx = dx / distance
                        ny = dy / distance
                        nz = dz / distance
                        move_x = nx * overlap * 0.5
                        move_y = ny * overlap * 0.5
                        move_z = nz * overlap * 0.5
                        obj1.x_pos -= move_x
                        obj1.y_pos -= move_y
                        obj1.z_pos -= move_z
                        obj2.x_pos += move_x
                        obj2.y_pos += move_y
                        obj2.z_pos += move_z
                        rvx = obj2.vx - obj1.vx
                        rvy = obj2.vy - obj1.vy
                        rvz = obj2.vz - obj1.vz
                        vel_along_normal = rvx * nx + rvy * ny + rvz * nz
                        if vel_along_normal > 0: continue
                        e = 0.95
                        j_impulse = -(1 + e) * vel_along_normal
                        j_impulse /= (1/obj1.mass) + (1/obj2.mass)
                        impulse_x = j_impulse * nx
                        impulse_y = j_impulse * ny
                        impulse_z = j_impulse * nz
                        obj1.vx -= impulse_x / obj1.mass
                        obj1.vy -= impulse_y / obj1.mass
                        obj1.vz -= impulse_z / obj1.mass
                        obj2.vx += impulse_x / obj2.mass
                        obj2.vy += impulse_y / obj2.mass
                        obj2.vz += impulse_z / obj2.mass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhysicsSim()
    window.show()
    sys.exit(app.exec_())