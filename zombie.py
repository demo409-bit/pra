
🧟 Zombie chases player
💥 Game Over on collision
🔁 Press **R to restart**
🖥 Game Over text on screen


---

# 🟢 PART 1: CREATE PROJECT

### ➤ Steps

1. Open Godot
2. Click **New Project**
3. Name: `HungryZombie`
4. Choose folder
5. Click **Create & Edit**

---

# 🟢 PART 2: CREATE MAIN SCENE

### ➤ Steps

1. Click **+ Add Node**
2. Search → `Node2D`
3. Click **Create**
4. Rename it → `Main`

---

# 🟢 PART 3: ADD PLAYER

## ➤ 3.1 Create Player Node

1. Select `Main`
2. Click **+ Add Child Node**
3. Search → `CharacterBody2D`
4. Click **Create**
5. Rename → `Player`

---

## ➤ 3.2 Add Sprite

1. Select `Player`
2. Click **+ Add Child Node**
3. Select `Sprite2D`
4. In Inspector → Texture → Load image

---

## ➤ 3.3 Add Collision

1. Select `Player`
2. Add child → `CollisionShape2D`
3. Inspector → Shape → New RectangleShape2D
4. Resize using mouse

---

## ➤ 3.4 Attach Player Script

1. Select `Player`
2. Click **Attach Script**
3. Click **Create**

### Paste:

```gdscript
extends CharacterBody2D

@export var speed = 200

func _physics_process(delta):
	var game = get_tree().get_first_node_in_group("game")
	if game != null and game.is_game_over:
		return
	
	var direction = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x += 1
	if Input.is_action_pressed("ui_left"):
		direction.x -= 1
	if Input.is_action_pressed("ui_down"):
		direction.y += 1
	if Input.is_action_pressed("ui_up"):
		direction.y -= 1
	
	velocity = direction.normalized() * speed
	move_and_slide()
```

---

# 🟢 PART 4: ADD ZOMBIE

## ➤ 4.1 Create Zombie

1. Select `Main`
2. Add child → `CharacterBody2D`
3. Rename → `Zombie`

---

## ➤ 4.2 Add Sprite

* Same steps as Player

---

## ➤ 4.3 Add Collision

* Same steps as Player

---

## ➤ 4.4 Add Area2D (IMPORTANT)

1. Select `Zombie`
2. Add child → `Area2D`
3. Add child to Area2D → `CollisionShape2D`
4. Set shape → RectangleShape2D
5. Make it slightly bigger than zombie

---

## ➤ 4.5 Attach Zombie Script

Paste:

```gdscript
extends CharacterBody2D

@export var speed = 100
@onready var player = get_parent().get_node("Player")

var game_over = false

func _physics_process(delta):
	if game_over:
		return
	
	if player != null:
		var direction = (player.global_position - global_position).normalized()
		
		velocity = direction * speed
		move_and_slide()
		
		rotation = direction.angle()

func _on_area_2d_body_entered(body):
	if body.name == "Player" and not game_over:
		game_over = true
		get_tree().call_group("game", "end_game")
```

---

# 🟢 PART 5: CONNECT SIGNAL (VERY IMPORTANT)

### ➤ Steps

1. Select `Area2D` (inside Zombie)
2. Go to right panel → **Node tab**
3. Find → `body_entered`
4. Double-click it
5. Connect to → `Zombie`
6. Click **Connect**

---

# 🟢 PART 6: ADD GAME OVER TEXT

## ➤ 6.1 Add Label

1. Select `Main`
2. Add child → `Label`
3. Rename → `GameOverText`

---

## ➤ 6.2 Set Text

Inspector → Text:

```
GAME OVER
Press R to Restart
```

---

## ➤ 6.3 Center It

Top toolbar → **Layout → Center**

---

## ➤ 6.4 Increase Size

Inspector → Theme Overrides → Font Size → 40+

---

## ➤ 6.5 Hide Initially

Uncheck ✅ Visible

---

# 🟢 PART 7: MAIN SCRIPT

## ➤ Attach script to `Main`

Paste:

```gdscript
extends Node2D

var is_game_over = false

func _ready():
	add_to_group("game")
	$GameOverText.visible = false

func end_game():
	is_game_over = true
	$GameOverText.visible = true

func _process(delta):
	if is_game_over and Input.is_key_pressed(KEY_R):
		get_tree().reload_current_scene()
```

---

# 🟢 PART 8: POSITION OBJECTS

### ➤ Move Player

* Select Player → drag left

### ➤ Move Zombie

* Select Zombie → drag right

---

# 🟢 PART 9: SAVE SCENE

1. Click **Scene → Save As**
2. Name → `Main.tscn`

---

# 🟢 PART 10: SET MAIN SCENE

If popup appears → click **Select Current**

OR manually:

* Project → Project Settings → Run → Main Scene → select `Main.tscn`

---

# 🟢 PART 11: RUN GAME 🎮

Click ▶ Play

---

# 🎯 FINAL OUTPUT

✔ Player moves
✔ Zombie follows
✔ Collision → GAME OVER text appears
✔ Press **R → Restart**

---

# 🚨 COMMON ERRORS (CHECK THIS)

❌ Node name not exactly `GameOverText`
❌ Signal not connected
❌ Player not named `"Player"`
❌ Label not inside Main

---

