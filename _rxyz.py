#_rxyz.py
import math
from rich import print as rp
import hashlib
from PIL import Image
__all__ = [
	"_rxyz", "Map2D10"
]
global w
global x
global y
global z
class _rxyz:
	def _xy(x=0, y=0):
		return (float(x), float(y))
	def _xyz(x=0, y=0, z=0):
		return (float(x), float(y), float(z))
	def _wxyz(w=0, x=0, y=0, z=0):
		return (float(w), float(x), float(y), float(z))
	def _add(a, b):
		return tuple(ai + bi for ai, bi in zip(a, b))
	def _sub(a, b):
		return tuple(ai - bi for ai, bi in zip(a, b))
	def _scale(v, s):
		s = float(s)
		return tuple(vi * s for vi in v)
	def _dot(a, b):
		return sum(float(ai) * float(bi) for ai, bi in zip(a, b))
	def _mag(v):
		return math.sqrt(sum(float(vi) * float(vi) for vi in v))
	def _normalize(v):
		m = _rxyz._mag(v)
		return v if m == 0 else tuple(float(vi) / m for vi in v)
	def _cross(a, b):
		try:
			ax, ay, az = a
			bx, by, bz = b
			return (ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)
		except Exception:
			return None
	def _dist(a, b):
		return math.sqrt(sum((float(ai) - float(bi)) ** 2 for ai, bi in zip(a, b)))
	def _lerp(a, b, t=0.5):
		t = float(t)
		return tuple(float(ai) + (float(bi) - float(ai)) * t for ai, bi in zip(a, b))
	def _angle(a, b):
		d = _rxyz._dot(a, b)
		ma = _rxyz._mag(a)
		mb = _rxyz._mag(b)
		if ma == 0 or mb == 0: return 0.0
		val = max(min(d / (ma * mb), 1.0), -1.0)
		return math.degrees(math.acos(val))
	def _reflect(v, n):
		n = _rxyz._normalize(n)
		dot = 2 * _rxyz._dot(v, n)
		return tuple(float(vi) - dot * float(ni) for vi, ni in zip(v, n))
	def _midpoint(a, b):
		return tuple((float(ai) + float(bi)) / 2.0 for ai, bi in zip(a, b))
	def _mix(*vectors):
		if not vectors: return ()
		n = len(vectors)
		size = len(vectors[0])
		return tuple(sum(float(v[i]) for v in vectors) / n for i in range(size))
	def _bbox(points):
		xs = []
		ys = []
		zs = []
		for p in points:
			if len(p) >= 1: xs.append(p[0])
			if len(p) >= 2: ys.append(p[1])
			if len(p) >= 3: zs.append(p[2])
		if not xs or not ys:
			return None
		if not zs:
			return ((min(xs), min(ys)), (max(xs), max(ys)))
		return ((min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs)))
	def _to_tuple(seq, dim=None):
		seq = list(seq)
		if dim is None: return tuple(float(x) for x in seq)
		seq = seq[:dim] + [0.0] * max(0, dim - len(seq))
		return tuple(float(x) for x in seq)
	def _convert(v, dim=3):
		return _rxyz._to_tuple(v, dim)
	def _3dto2d(v):
		return _rxyz._to_tuple(v, 2)
	def _2dto3d(v, z=0.0):
		x, y = v
		return (float(x), float(y), float(z))
	def _3dto4d(v, w=1.0):
		x, y, z = v
		return (float(w), float(x), float(y), float(z))
	def _4dto3d(v):
		_, x, y, z = v
		return (float(x), float(y), float(z))
	def _xy_to_polar(v):
		x, y = v
		r = math.hypot(x, y)
		theta = math.degrees(math.atan2(y, x))
		return (r, theta)
	def _polar_to_xy(r, theta_deg):
		r = float(r)
		t = math.radians(float(theta_deg))
		return (r * math.cos(t), r * math.sin(t))
	def _rotate2d(v, deg):
		x, y = v
		r = math.radians(float(deg))
		c = math.cos(r)
		s = math.sin(r)
		return (x * c - y * s, x * s + y * c)
	def _mat3_identity():
		return [
			[1.0, 0.0, 0.0],
			[0.0, 1.0, 0.0],
			[0.0, 0.0, 1.0]
		]
	def _mat4_identity():
		return [
			[1.0, 0.0, 0.0, 0.0],
			[0.0, 1.0, 0.0, 0.0],
			[0.0, 0.0, 1.0, 0.0],
			[0.0, 0.0, 0.0, 1.0]
		]
	def _rotX(deg):
		r = math.radians(float(deg))
		c = math.cos(r)
		s = math.sin(r)
		return [
			[1.0, 0.0, 0.0],
			[0.0,  c, -s],
			[0.0,  s,  c]
		]
	def _rotY(deg):
		r = math.radians(float(deg))
		c = math.cos(r)
		s = math.sin(r)
		return [
			[ c, 0.0,  s],
			[0.0, 1.0, 0.0],
			[-s, 0.0,  c]
		]
	def _rotZ(deg):
		r = math.radians(float(deg))
		c = math.cos(r)
		s = math.sin(r)
		return [
			[ c, -s, 0.0],
			[ s,  c, 0.0],
			[0.0, 0.0, 1.0]
		]
	def _mat_mul(a, b):
		h = len(a)
		w = len(b[0])
		n = len(b)
		return [
			[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(w)]
			for i in range(h)
		]
	def _mat3_mul_vec(m, v):
		v3 = _rxyz._to_tuple(v, 3)
		x = m[0][0] * v3[0] + m[0][1] * v3[1] + m[0][2] * v3[2]
		y = m[1][0] * v3[0] + m[1][1] * v3[1] + m[1][2] * v3[2]
		z = m[2][0] * v3[0] + m[2][1] * v3[1] + m[2][2] * v3[2]
		return (x, y, z)
	def _mat4_mul_vec(m, v):
		v4 = _rxyz._to_tuple(v, 4)
		w = m[0][0] * v4[0] + m[0][1] * v4[1] + m[0][2] * v4[2] + m[0][3] * v4[3]
		x = m[1][0] * v4[0] + m[1][1] * v4[1] + m[1][2] * v4[2] + m[1][3] * v4[3]
		y = m[2][0] * v4[0] + m[2][1] * v4[1] + m[2][2] * v4[2] + m[2][3] * v4[3]
		z = m[3][0] * v4[0] + m[3][1] * v4[1] + m[3][2] * v4[2] + m[3][3] * v4[3]
		return (w, x, y, z)
	def _translate(tx=0, ty=0, tz=0):
		m = _rxyz._mat4_identity()
		m[0][3] = float(tx)
		m[1][3] = float(ty)
		m[2][3] = float(tz)
		return m
	def _scale4(sx=1, sy=1, sz=1):
		m = _rxyz._mat4_identity()
		m[0][0] = float(sx)
		m[1][1] = float(sy)
		m[2][2] = float(sz)
		return m
	def _perspective(fov, aspect, near, far):
		f = 1.0 / math.tan(math.radians(float(fov)) / 2.0)
		nf = 1.0 / (float(near) - float(far))
		return [
			[f / float(aspect), 0.0, 0.0,                          0.0],
			[0.0,               f,   0.0,                          0.0],
			[0.0,               0.0, (float(far) + float(near)) * nf, 2.0 * float(far) * float(near) * nf],
			[0.0,               0.0, -1.0,                         0.0]
		]
	def _project_3dto2d(v3, proj_mat, viewport=(0, 0, 1, 1)):
		v4 = (v3[0], v3[1], v3[2], 1.0)
		tx, ty, tz, tw = _rxyz._mat4_mul_vec(proj_mat, v4)
		if tw == 0: return None
		nx = tx / tw
		ny = ty / tw
		vx, vy, vw, vh = viewport
		sx = vx + (nx + 1.0) * 0.5 * vw
		sy = vy + (1.0 - (ny + 1.0) * 0.5) * vh
		return (sx, sy)
	def _quat_mul(q1, q2):
		w1, x1, y1, z1 = q1
		w2, x2, y2, z2 = q2
		w = w1*w2 - x1*x2 - y1*y2 - z1*z2
		x = w1*x2 + x1*w2 + y1*z2 - z1*y2
		y = w1*y2 - x1*z2 + y1*w2 + z1*x2
		z = w1*z2 + x1*y2 - y1*x2 + z1*w2
		return (w, x, y, z)
	def _quat_rot(axis, deg):
		ax, ay, az = _rxyz._normalize(axis)
		r = math.radians(float(deg) / 2.0)
		s = math.sin(r)
		return (math.cos(r), ax * s, ay * s, az * s)
	def _quat_apply(q, v):
		qv = (0.0, float(v[0]), float(v[1]), float(v[2]))
		qc = _rxyz._quat_mul(_rxyz._quat_mul(q, qv), _rxyz._quat_conj(q))
		return (qc[1], qc[2], qc[3])
	def _quat_conj(q):
		w, x, y, z = q
		return (w, -x, -y, -z)
	def _print(label, value):
		rp(label, value)
	def setw(fw=float):
		w = fw
	def setx(fy=float):
		x = fy
	def sety(fy=float):
		y = fy
	def setz(fz=float):
		z = fz
def h8(value: str) -> str:
    return hashlib.sha256(str(value).encode()).hexdigest()[:8]
class Map2D10:
    def __init__(self, data, **materials):
        """
        data: flat list of block IDs (strings)
        materials: m0="grass", m1="stone", etc.
        Each material may include: name, color=(r,g,b)
        Example:
            m0={"name":"grass","color":(34,139,34)}
        """
        self.data = data
        self.materials = materials
        self.row_width = 10
    def block_id(self, block):
        for key, value in self.materials.items():
            if isinstance(value, dict):
                if value.get("name") == block: return key
            else:
                if value == block: return key
        return "unknown"
    def block_color(self, block):
        for key, value in self.materials.items():
            if isinstance(value, dict):
                if value.get("name") == block:
                    return value.get("color", (255, 0, 255))
            else:
                if value == block:
                    return (255, 0, 255)
        return (255, 0, 255)
    def analyze(self):
        for index, block in enumerate(self.data):
            x = index % self.row_width
            y = index // self.row_width
            block_hash = h8(block)
            x_hash = h8(x)
            y_hash = h8(y)
            full_hash = block_hash[:4] + x_hash[:2] + y_hash[:2]
            rp(f"Block '{block}' ({x}, {y})")
            rp(" - Full Position Details")
            rp(f"  - block '{block}'")
            rp(f"  - reg {x}, {y}")
            rp(f"  - hash {block_hash}")
            rp(f"  - xhash {x_hash}")
            rp(f"  - yhash {y_hash}")
            rp(f"  - fhash {full_hash}")
            rp(f" - Block ID: {self.block_id(block)}")
            rp()
    def exportpng(self, filename="map.png", pixel_size=20):
        width = self.row_width
        height = len(self.data) // self.row_width
        img = Image.new("RGB", (width * pixel_size, height * pixel_size))
        px = img.load()
        for index, block in enumerate(self.data):
            x = index % width
            y = index // width
            color = self.block_color(block)
            for py in range(pixel_size):
                for pxl in range(pixel_size):
                    px[x * pixel_size + pxl, y * pixel_size + py] = color
        img.save(filename)
        rp(f"PNG Exported: {filename}")
#e.x.
#lst = [
#     "0","1","2","3","4","5","6","7","8","9",
#     "1","1","0","3","2","2","4","5","8","9",
#     "7","7","7","2","1","0","0","4","3","3"
#]
#mapper = Map2D10(
#    lst,
#    m0={"name":"0", "color":(50,50,50)},
#    m1={"name":"1", "color":(0,200,0)},
#    m2={"name":"2", "color":(150,75,0)},
#    m3={"name":"3", "color":(255,215,0)},
#    m4={"name":"4", "color":(200,0,0)},
#    m5={"name":"5", "color":(0,0,200)},
#    m6={"name":"6", "color":(255,140,0)},
#    m7={"name":"7", "color":(128,0,128)},
#    m8={"name":"8", "color":(0,255,255)},
#    m9={"name":"9", "color":(255,20,147)}
#)
## export PNG
#mapper.exportpng("my_map.png", pixel_size=20)
#mapper.analyze()