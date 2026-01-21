# Scratch API Reference

Scratch block emulation (motion, looks, sound).

## Import

```python
from stamp.scratch import Motion, Looks, Sound
```

## Overview

Stamp emulates Scratch programming blocks for motion, looks, and sound operations.

## Motion Class

Sprite movement and position.

### Motion.move(steps)

Move sprite forward.

**Parameters:**
- `steps` (int): Number of steps to move

```python
from stamp.scratch import Motion

Motion.move(10)  # Move 10 steps forward
```

### Motion.rotate(degrees)

Rotate sprite.

**Parameters:**
- `degrees` (int): Degrees to rotate (positive = clockwise, negative = counter-clockwise)

```python
from stamp.scratch import Motion

Motion.rotate(90)   # Rotate 90 degrees clockwise
Motion.rotate(-45)  # Rotate 45 degrees counter-clockwise
```

### Motion.goto(x, y)

Go to specific position.

**Parameters:**
- `x` (int): X coordinate
- `y` (int): Y coordinate

```python
from stamp.scratch import Motion

Motion.goto(100, 50)  # Move to (100, 50)
```

### Motion.glide(x, y, seconds)

Glide to position over time.

**Parameters:**
- `x` (int): X coordinate
- `y` (int): Y coordinate
- `seconds` (int): Duration in seconds

```python
from stamp.scratch import Motion

Motion.glide(200, 100, 2)  # Glide to (200, 100) over 2 seconds
```

### Motion.point_in_direction(degrees)

Point sprite in direction.

**Parameters:**
- `degrees` (int): Direction in degrees

```python
from stamp.scratch import Motion

Motion.point_in_direction(90)  # Point to the right
Motion.point_in_direction(180) # Point down
```

### Motion.point_towards(x, y)

Point sprite towards position.

**Parameters:**
- `x` (int): X coordinate
- `y` (int): Y coordinate

```python
from stamp.scratch import Motion

Motion.point_towards(100, 100)  # Point towards (100, 100)
```

### Motion.change_x_by(dx)

Change X position.

**Parameters:**
- `dx` (int): Amount to change X

```python
from stamp.scratch import Motion

Motion.change_x_by(10)   # Move right 10
Motion.change_x_by(-5)  # Move left 5
```

### Motion.set_x(x)

Set X position.

**Parameters:**
- `x` (int): X coordinate

```python
from stamp.scratch import Motion

Motion.set_x(100)  # Set X to 100
```

### Motion.change_y_by(dy)

Change Y position.

**Parameters:**
- `dy` (int): Amount to change Y

```python
from stamp.scratch import Motion

Motion.change_y_by(10)   # Move up 10
Motion.change_y_by(-5)  # Move down 5
```

### Motion.set_y(y)

Set Y position.

**Parameters:**
- `y` (int): Y coordinate

```python
from stamp.scratch import Motion

Motion.set_y(50)  # Set Y to 50
```

### Motion.bounce_on_edge()

Bounce if on edge.

```python
from stamp.scratch import Motion

Motion.bounce_on_edge()
```

### Motion.get_x()

Get X position.

**Returns:** int - X coordinate

```python
from stamp.scratch import Motion

x = Motion.get_x()
print(f"X position: {x}")
```

### Motion.get_y()

Get Y position.

**Returns:** int - Y coordinate

```python
from stamp.scratch import Motion

y = Motion.get_y()
print(f"Y position: {y}")
```

### Motion.get_direction()

Get direction.

**Returns:** int - Direction in degrees

```python
from stamp.scratch import Motion

direction = Motion.get_direction()
print(f"Direction: {direction} degrees")
```

## Looks Class

Sprite appearance and effects.

### Looks.show()

Show sprite.

```python
from stamp.scratch import Looks

Looks.show()
```

### Looks.hide()

Hide sprite.

```python
from stamp.scratch import Looks

Looks.hide()
```

### Looks.switch_costume(costume_name)

Switch to costume.

**Parameters:**
- `costume_name` (str): Name of costume

```python
from stamp.scratch import Looks

Looks.switch_costume("costume1")
```

### Looks.next_costume()

Switch to next costume.

```python
from stamp.scratch import Looks

Looks.next_costume()
```

### Looks.say(message, seconds=None)

Say speech bubble.

**Parameters:**
- `message` (str): Message to say
- `seconds` (int): Duration in seconds (optional)

```python
from stamp.scratch import Looks

Looks.say("Hello!")
Looks.say("Hello, World!", 2)  # Say for 2 seconds
```

### Looks.think(message, seconds=None)

Think thought bubble.

**Parameters:**
- `message` (str): Message to think
- `seconds` (int): Duration in seconds (optional)

```python
from stamp.scratch import Looks

Looks.think("Hmm...")
Looks.think("I'm thinking...", 3)  # Think for 3 seconds
```

### Looks.change_effect(effect, amount)

Change effect.

**Parameters:**
- `effect` (str): Effect name ("color", "brightness", "ghost", etc.)
- `amount` (int): Amount to change

```python
from stamp.scratch import Looks

Looks.change_effect("color", 25)
Looks.change_effect("brightness", 10)
```

### Looks.set_effect(effect, amount)

Set effect.

**Parameters:**
- `effect` (str): Effect name
- `amount` (int): Effect value

```python
from stamp.scratch import Looks

Looks.set_effect("color", 50)
Looks.set_effect("ghost", 100)
```

### Looks.clear_effects()

Clear all effects.

```python
from stamp.scratch import Looks

Looks.clear_effects()
```

### Looks.change_size(size_amount)

Change size.

**Parameters:**
- `size_amount` (int): Amount to change size

```python
from stamp.scratch import Looks

Looks.change_size(10)   # Increase size by 10%
Looks.change_size(-5)  # Decrease size by 5%
```

### Looks.set_size(size)

Set size.

**Parameters:**
- `size` (int): Size percentage

```python
from stamp.scratch import Looks

Looks.set_size(100)  # Set size to 100%
Looks.set_size(150)  # Set size to 150%
```

### Looks.go_to_front()

Move sprite to front.

```python
from stamp.scratch import Looks

Looks.go_to_front()
```

### Looks.go_back(layers)

Move sprite back.

**Parameters:**
- `layers` (int): Number of layers to move back

```python
from stamp.scratch import Looks

Looks.go_back(1)   # Move back 1 layer
Looks.go_back(3)   # Move back 3 layers
```

### Looks.go_to_layer(layer)

Go to specific layer.

**Parameters:**
- `layer` (int): Layer number (front = 1, higher = back)

```python
from stamp.scratch import Looks

Looks.go_to_layer(1)  # Go to front
Looks.go_to_layer(5)  # Go to layer 5
```

## Sound Class

Sound playback and effects.

### Sound.play(sound_name)

Play sound.

**Parameters:**
- `sound_name` (str): Name of sound

```python
from stamp.scratch import Sound

Sound.play("meow")
Sound.play("pop")
```

### Sound.play_until_done(sound_name)

Play sound until finished.

**Parameters:**
- `sound_name` (str): Name of sound

```python
from stamp.scratch import Sound

Sound.play_until_done("drum")
```

### Sound.stop_all_sounds()

Stop all sounds.

```python
from stamp.scratch import Sound

Sound.stop_all_sounds()
```

### Sound.volume(amount)

Set volume.

**Parameters:**
- `amount` (int): Volume percentage (0-100)

```python
from stamp.scratch import Sound

Sound.volume(100)  # Full volume
Sound.volume(50)   # 50% volume
```

### Sound.change_volume(amount)

Change volume.

**Parameters:**
- `amount` (int): Amount to change volume

```python
from stamp.scratch import Sound

Sound.change_volume(10)   # Increase volume
Sound.change_volume(-5)  # Decrease volume
```

## Usage Examples

### Basic Movement

```python
from stamp.scratch import Motion

# Move sprite
Motion.move(10)
Motion.rotate(90)
Motion.move(10)

# Position
Motion.goto(0, 0)
Motion.glide(100, 100, 2)
```

### Animation Loop

```python
from stamp.scratch import Motion, Looks

# Move and say
for i in range(10):
    Motion.move(10)
    Looks.say("Moving!")
    Looks.next_costume()
```

### Interactive Sprite

```python
from stamp.scratch import Motion, Looks

# Draw square
Motion.goto(0, 0)
for _ in range(4):
    Motion.move(100)
    Motion.rotate(90)
    Looks.say("Side done!", 1)
```

### Sound Effects

```python
from stamp.scratch import Sound, Motion

# Play sound while moving
Sound.play("pop")
Motion.move(100)
Sound.play_until_done("drum")
```

### Visual Effects

```python
from stamp.scratch import Looks

# Apply effects
Looks.change_effect("color", 25)
Looks.change_effect("ghost", 50)
Looks.say("Spooky!", 2)
Looks.clear_effects()
```

### Size Changes

```python
from stamp.scratch import Looks

# Change size
Looks.set_size(100)
for i in range(10):
    Looks.change_size(10)
    Looks.say(f"Size: {100 + i * 10}%")
```

### Layer Management

```python
from stamp.scratch import Looks

# Manage layers
Looks.go_to_front()
Looks.go_back(2)
Looks.go_to_layer(5)
```

### Complete Animation

```python
from stamp.scratch import Motion, Looks, Sound

# Start at origin
Motion.goto(0, 0)
Looks.show()
Looks.set_size(100)

# Play sound
Sound.play("pop")

# Animation loop
for i in range(10):
    Motion.move(20)
    Motion.rotate(36)
    Looks.next_costume()
    Looks.say(f"Step {i + 1}", 0.5)
    Looks.change_effect("color", 10)

# End
Looks.clear_effects()
Looks.go_to_front()
Looks.say("Done!", 2)
```

## Notes

- Motion: 0 degrees = up, 90 = right, 180 = down, 270 = left
- Looks effects include: color, brightness, ghost, fisheye, whirl, pixelate, mosaic
- Sound volume: 0 = mute, 100 = full volume
- Layers: 1 = front, higher numbers = back
- Coordinates: (0, 0) is center, positive X = right, positive Y = up
- Costume changes cycle through available costumes

---

See [Scratch Examples](../examples/scratch-demo.md) for more examples.
