# Physics API Reference

3D physics simulation with OpenGL.

## Import

```python
from stamp.physics import PhysicsSim, PhysicsObject
```

## Overview

Stamp's physics engine provides 3D physics simulation with OpenGL rendering. Includes collision detection, gravity, velocity, and position tracking.

## PhysicsSim Class

Main simulation class for managing physics objects and rendering.

### PhysicsSim.__init__(width=800, height=600, fps=60)

Initialize physics simulation.

**Parameters:**
- `width` (int): Window width in pixels (default: 800)
- `height` (int): Window height in pixels (default: 600)
- `fps` (int): Frames per second (default: 60)

```python
from stamp.physics import PhysicsSim

# Create simulation
sim = PhysicsSim(width=800, height=600, fps=60)
```

### PhysicsSim.add_object(obj)

Add physics object to simulation.

**Parameters:**
- `obj` (PhysicsObject): Physics object to add

```python
from stamp.physics import PhysicsSim, PhysicsObject

sim = PhysicsSim()
obj = PhysicsObject(x=0, y=0, z=0)
sim.add_object(obj)
```

### PhysicsSim.remove_object(obj)

Remove physics object from simulation.

**Parameters:**
- `obj` (PhysicsObject): Physics object to remove

```python
sim.remove_object(obj)
```

### PhysicsSim.update(dt)

Update simulation by time step.

**Parameters:**
- `dt` (float): Time delta in seconds

```python
import time

sim = PhysicsSim()

while True:
    dt = time.time() - last_time
    sim.update(dt)
    last_time = time.time()
```

### PhysicsSim.render()

Render all objects in simulation.

```python
sim = PhysicsSim()

while True:
    sim.update(0.016)  # ~60 FPS
    sim.render()
```

### PhysicsSim.set_gravity(x, y, z)

Set global gravity.

**Parameters:**
- `x` (float): Gravity X component
- `y` (float): Gravity Y component
- `z` (float): Gravity Z component

```python
sim = PhysicsSim()
sim.set_gravity(0, -9.8, 0)  # Standard gravity
```

### PhysicsSim.run()

Start main simulation loop.

```python
sim = PhysicsSim()
sim.add_object(obj)
sim.run()
```

### PhysicsSim.stop()

Stop simulation.

```python
sim.stop()
```

## PhysicsObject Class

Represents a physical object in simulation.

### PhysicsObject.__init__(x=0, y=0, z=0, mass=1.0, vx=0, vy=0, vz=0)

Create physics object.

**Parameters:**
- `x` (float): X position (default: 0)
- `y` (float): Y position (default: 0)
- `z` (float): Z position (default: 0)
- `mass` (float): Object mass (default: 1.0)
- `vx` (float): X velocity (default: 0)
- `vy` (float): Y velocity (default: 0)
- `vz` (float): Z velocity (default: 0)

```python
from stamp.physics import PhysicsObject

# Create object at origin
obj = PhysicsObject(x=0, y=0, z=0)

# Create object with mass and velocity
obj = PhysicsObject(
    x=10, y=20, z=5,
    mass=5.0,
    vx=1, vy=2, vz=0
)
```

### PhysicsObject.set_position(x, y, z)

Set object position.

**Parameters:**
- `x` (float): X position
- `y` (float): Y position
- `z` (float): Z position

```python
obj.set_position(10, 20, 5)
```

### PhysicsObject.get_position()

Get object position.

**Returns:** tuple - (x, y, z)

```python
x, y, z = obj.get_position()
print(f"Position: ({x}, {y}, {z})")
```

### PhysicsObject.set_velocity(vx, vy, vz)

Set object velocity.

**Parameters:**
- `vx` (float): X velocity
- `vy` (float): Y velocity
- `vz` (float): Z velocity

```python
obj.set_velocity(1, 0, 0)
```

### PhysicsObject.get_velocity()

Get object velocity.

**Returns:** tuple - (vx, vy, vz)

```python
vx, vy, vz = obj.get_velocity()
print(f"Velocity: ({vx}, {vy}, {vz})")
```

### PhysicsObject.set_mass(mass)

Set object mass.

**Parameters:**
- `mass` (float): Object mass

```python
obj.set_mass(10.0)
```

### PhysicsObject.get_mass()

Get object mass.

**Returns:** float - Object mass

```python
mass = obj.get_mass()
print(f"Mass: {mass}")
```

### PhysicsObject.apply_force(fx, fy, fz)

Apply force to object.

**Parameters:**
- `fx` (float): Force X component
- `fy` (float): Force Y component
- `fz` (float): Force Z component

```python
obj.apply_force(10, 0, 0)  # Apply force in X direction
```

### PhysicsObject.update(dt, gravity=(0, -9.8, 0))

Update object physics.

**Parameters:**
- `dt` (float): Time delta
- `gravity` (tuple): Gravity vector (default: (0, -9.8, 0))

```python
obj.update(0.016, gravity=(0, -9.8, 0))
```

## Usage Examples

### Basic Simulation

```python
from stamp.physics import PhysicsSim, PhysicsObject

# Create simulation
sim = PhysicsSim(width=800, height=600, fps=60)

# Create object
obj = PhysicsObject(x=0, y=100, z=0, mass=1.0)
sim.add_object(obj)

# Run simulation
sim.run()
```

### Falling Object

```python
from stamp.physics import PhysicsSim, PhysicsObject

sim = PhysicsSim()

# Create falling object
obj = PhysicsObject(x=0, y=100, z=0, mass=1.0)
sim.set_gravity(0, -9.8, 0)
sim.add_object(obj)

sim.run()
```

### Multiple Objects

```python
from stamp.physics import PhysicsSim, PhysicsObject

sim = PhysicsSim()

# Create multiple objects
obj1 = PhysicsObject(x=-10, y=100, z=0, mass=1.0)
obj2 = PhysicsObject(x=0, y=100, z=0, mass=2.0)
obj3 = PhysicsObject(x=10, y=100, z=0, mass=1.5)

sim.add_object(obj1)
sim.add_object(obj2)
sim.add_object(obj3)

sim.run()
```

### Custom Update Loop

```python
from stamp.physics import PhysicsSim, PhysicsObject
import time

sim = PhysicsSim()
obj = PhysicsObject(x=0, y=100, z=0, mass=1.0)
sim.add_object(obj)

last_time = time.time()

while True:
    dt = time.time() - last_time
    sim.update(dt)
    sim.render()
    last_time = time.time()
```

### Applying Forces

```python
from stamp.physics import PhysicsSim, PhysicsObject

sim = PhysicsSim()
obj = PhysicsObject(x=0, y=0, z=0, mass=1.0)
sim.add_object(obj)

# Apply upward force
obj.apply_force(0, 50, 0)

sim.run()
```

## Physics Concepts

### Velocity

Velocity is the rate of change of position. Objects can have velocity in 3D space:

```python
obj.set_velocity(vx=1, vy=2, vz=0.5)
```

### Mass

Mass determines how much force is needed to accelerate an object:

```python
obj.set_mass(5.0)  # Heavier object
```

### Gravity

Gravity applies constant downward acceleration:

```python
sim.set_gravity(0, -9.8, 0)  # Earth gravity
```

### Force

Force causes acceleration proportional to mass:

```python
obj.apply_force(fx=10, fy=0, fz=0)
```

## Notes

- Physics uses OpenGL for rendering
- Default gravity is (0, -9.8, 0) - Earth gravity
- Time step (dt) should be in seconds
- Mass is in kg, position in meters, velocity in m/s
- Collision detection may vary by implementation

---

See [Physics Demo](../examples/physics-demo.md) for complete examples.
See [Physics Guide](../guides/physics-guide.md) for detailed guide.
