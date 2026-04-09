Perfect — this is a classic **platformer (jumping game)** and a great step up 🔥
I’ll guide you **from scratch with full navigation + final working scripts**.

---

# 🎮 Rooftop Leap (Jumping Game) – Full Godot Guide

## 🧩 What you’ll build:

✔ Player runs & jumps
✔ Cannot jump mid-air
✔ Platforms (rooftops)
✔ Falling = Game Over
✔ Reach goal = WIN
✔ Labels (Score/Status)
✔ Restart button
✔ Press **R** to restart

---

# 🧱 STEP 1: Create Project

1. Open **Godot**
2. Click **New Project**
3. Name: `RooftopLeap`
4. Click **Create & Edit**

---

# 🏙️ STEP 2: Create Main Scene

1. Click **+ Add Node**
2. Select `Node2D`
3. Rename → `Main`
4. Save → `main.tscn`

---

# 🧍 STEP 3: Create Player

## ➤ Add Player Node

1. Right-click **Main**
2. Add Child → `CharacterBody2D`
3. Rename → `Player`

---

## ➤ Add Components

Inside Player:

* `Sprite2D`
* `CollisionShape2D` → RectangleShape2D

---

## ➤ Attach Script (IMPORTANT)

```gdscript
extends CharacterBody2D

const SPEED = 200
const JUMP_FORCE = -400
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta):
	# Apply gravity
	if not is_on_floor():
		velocity.y += gravity * delta

	# Move left/right
	var direction = Input.get_axis("ui_left", "ui_right")
	velocity.x = direction * SPEED

	# Jump ONLY if on floor
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_FORCE

	move_and_slide()
```

---

# 🏢 STEP 4: Create Platforms (Rooftops)

## ➤ Add Floor

1. Right-click Main → Add `StaticBody2D`
2. Rename → `Ground`

Add inside Ground:

* `CollisionShape2D` → RectangleShape2D (wide)

---

## ➤ Add Rooftops

Repeat:

1. Add `StaticBody2D`
2. Rename → `Platform1`, `Platform2`, etc.

Inside each:

* `CollisionShape2D`

👉 Arrange them with **gaps** between platforms

---

# 🎯 STEP 5: Create Goal (WIN AREA)

## ➤ Add Goal Node

1. Add `Area2D`
2. Rename → `Goal`

Inside:

* `CollisionShape2D`
* `Sprite2D` (optional flag/door)

---

## ➤ Attach Script to Goal

```gdscript
extends Area2D

signal player_won

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("player_won")
```

---

## ➤ Connect Signal

1. Go to **Node tab**
2. Double-click `body_entered`
3. Connect → Goal

---

# 💀 STEP 6: Create Fall Detection (GAME OVER)

## ➤ Add Death Zone

1. Add `Area2D`
2. Rename → `DeathZone`

Place it **below screen**

---

## ➤ Script

```gdscript
extends Area2D

signal player_died

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("player_died")
```

---

# 🖥️ STEP 7: Add UI

## ➤ Add CanvasLayer

1. Right-click Main → Add `CanvasLayer`

---

## ➤ Add Labels

### Status Label

* Add `Label`
* Rename → `StatusLabel`
* Text → ""
* Visible = OFF

---

### Restart Button

* Add `Button`
* Rename → `RestartButton`
* Text → "Restart"
* Visible = OFF

---

# 🧠 STEP 8: Main Script (Game Logic)

Attach script to **Main**

```gdscript
extends Node2D

@onready var status_label = $CanvasLayer/StatusLabel
@onready var restart_button = $CanvasLayer/RestartButton

func _ready():
	pass

# WIN
func _on_goal_player_won():
	show_result("YOU WIN!")

# GAME OVER
func _on_deathzone_player_died():
	show_result("GAME OVER")

func show_result(text):
	status_label.text = text
	status_label.visible = true
	restart_button.visible = true
	get_tree().paused = true

# Restart button
func _on_restart_button_pressed():
	get_tree().paused = false
	get_tree().reload_current_scene()

# Press R
func _unhandled_input(event):
	if event.is_action_pressed("restart"):
		get_tree().paused = false
		get_tree().reload_current_scene()
```

---

# 🔗 STEP 9: CONNECT SIGNALS (VERY IMPORTANT)

## ➤ Goal → Main

1. Select **Goal**
2. Node tab → `player_won`
3. Connect → Main

---

## ➤ DeathZone → Main

1. Select **DeathZone**
2. Node tab → `player_died`
3. Connect → Main

---

## ➤ Restart Button

1. Select **RestartButton**
2. Node tab → `pressed()`
3. Connect → Main

---

# ⚠️ STEP 10: FIX BUTTON & INPUT

## ➤ Restart Button

Set:
👉 **Process Mode = Always**

---

## ➤ Main Node

Set:
👉 **Process Mode = Always**

---

# 🎮 STEP 11: ADD R KEY

Go to:

👉 **Project Settings → Input Map**

1. Add action: `restart`
2. Press **R key**

---

# 🧪 FINAL TEST

✔ Run game
✔ Move left/right
✔ Jump only on ground
✔ Fall → GAME OVER
✔ Reach goal → YOU WIN
✔ Restart button works
✔ Press R works

---

# 💥 FINAL SCRIPTS (ALL TOGETHER)

---

## 🧍 Player.gd

```gdscript
extends CharacterBody2D

const SPEED = 200
const JUMP_FORCE = -400
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

	var direction = Input.get_axis("ui_left", "ui_right")
	velocity.x = direction * SPEED

	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_FORCE

	move_and_slide()
```

---

## 🎯 Goal.gd

```gdscript
extends Area2D

signal player_won

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("player_won")
```

---

## 💀 DeathZone.gd

```gdscript
extends Area2D

signal player_died

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("player_died")
```

---

## 🧠 Main.gd

```gdscript
extends Node2D

@onready var status_label = $CanvasLayer/StatusLabel
@onready var restart_button = $CanvasLayer/RestartButton

func _on_goal_player_won():
	show_result("YOU WIN!")

func _on_deathzone_player_died():
	show_result("GAME OVER")

func show_result(text):
	status_label.text = text
	status_label.visible = true
	restart_button.visible = true
	get_tree().paused = true

func _on_restart_button_pressed():
	get_tree().paused = false
	get_tree().reload_current_scene()

func _unhandled_input(event):
	if event.is_action_pressed("restart"):
		get_tree().paused = false
		get_tree().reload_current_scene()
```

---

# 🎉 DONE!

You now have a **complete jumping rooftop game** 🚀

---

# 🚀 NEXT UPGRADE (if you want)

👉 Add **scrolling camera (endless runner)**
👉 Add **moving platforms**
👉 Add **score based on distance**
👉 Add **animations + sound**

Just tell me 👍
