 Deep Sea Treasure (Coin Collector)

# 🧱 STEP 1: Create New Project

1. Open **Godot**
2. Click **New Project**
3. Name: `DeepSeaTreasure`
4. Choose folder
5. Click **Create & Edit**

---

# 🌊 STEP 2: Create Main Scene

1. Click **+ (Add Node)**
2. Search: `Node2D`
3. Click → **Create**
4. Rename it → `Main`

👉 Save scene:

* Press **Ctrl + S**
* Name: `main.tscn`

---

# 🤿 STEP 3: Create Player

## ➤ Add Player Node

1. Right-click **Main**
2. Click **Add Child Node**
3. Select `CharacterBody2D`
4. Rename → `Player`

---

## ➤ Add Components

Inside Player:

1. Right-click Player → Add:

   * `Sprite2D`
   * `CollisionShape2D`

2. Click CollisionShape2D → Inspector → Shape:

   * Choose **RectangleShape2D**

---

## ➤ Attach Script

1. Select Player
2. Click **Attach Script**

Paste:

```gdscript
extends CharacterBody2D

const SPEED = 200

func _physics_process(delta):
	var direction = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x += 1
	if Input.is_action_pressed("ui_left"):
		direction.x -= 1
	if Input.is_action_pressed("ui_down"):
		direction.y += 1
	if Input.is_action_pressed("ui_up"):
		direction.y -= 1

	velocity = direction.normalized() * SPEED
	move_and_slide()
```

---

# 🪙 STEP 4: Create Coin Scene

## ➤ New Scene

1. Click **+ (top left)**
2. Add `Area2D`
3. Rename → `Coin`

---

## ➤ Add Components

Inside Coin:

* `Sprite2D`
* `CollisionShape2D`

---

## ➤ Attach Script

```gdscript
extends Area2D

signal collected

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("collected", global_position)
		queue_free()
```

---

## ➤ Connect Signal

1. Select Coin
2. Go to **Node tab (right)**
3. Double click: `body_entered`
4. Connect → Coin

---

## ➤ Save Scene

`coin.tscn`

---

# 🪙 STEP 5: Add Coins to Main

1. Open `main.tscn`
2. Drag `coin.tscn` into scene
3. Duplicate (Ctrl + D) → add 3–5 coins

---

## ➤ Add Coins to Group

For EACH coin:

1. Select coin
2. Go to **Node → Groups**
3. Add group: `coins`

---

# 🔢 STEP 6: Add UI

## ➤ Add CanvasLayer

1. Right-click Main → Add `CanvasLayer`

---

## ➤ Add Score Label

1. Add `Label`
2. Rename → `ScoreLabel`
3. Text → `Treasure: 0`

---

## ➤ Add Game Result Label

1. Add another `Label`
2. Rename → `GameOverLabel`
3. Text → `YOU WIN`
4. Set **Visible = OFF**

---

## ➤ Add Restart Button

1. Add `Button`
2. Rename → `RestartButton`
3. Text → `Restart`
4. Set **Visible = OFF**

---

# 🧠 STEP 7: Main Script (FULL GAME LOGIC)

Attach script to **Main**

```gdscript
extends Node2D

var score = 0
var max_score = 10

@onready var score_label = $CanvasLayer/ScoreLabel
@onready var game_over_label = $CanvasLayer/GameOverLabel
@onready var restart_button = $CanvasLayer/RestartButton

var coin_scene = preload("res://coin.tscn")

func _ready():
	randomize()
	update_score()
	connect_all_coins()

func connect_all_coins():
	for coin in get_tree().get_nodes_in_group("coins"):
		coin.connect("collected", Callable(self, "_on_coin_collected"))

func _on_coin_collected(pos):
	score += 1
	update_score()
	spawn_coin()

	if score >= max_score:
		show_game_result("YOU WIN!")

func spawn_coin():
	var coin = coin_scene.instantiate()
	add_child(coin)

	coin.position = Vector2(
		randf_range(50, 750),
		randf_range(50, 450)
	)

	coin.add_to_group("coins")
	coin.connect("collected", Callable(self, "_on_coin_collected"))

func update_score():
	score_label.text = "Treasure: " + str(score)

func show_game_result(text):
	game_over_label.text = text
	game_over_label.visible = true
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

# 🔁 STEP 8: Connect Restart Button

1. Select **RestartButton**
2. Go to **Node tab**
3. Double-click `pressed()`
4. Connect → Main

---

# ⚠️ STEP 9: Fix Button Not Working

1. Select RestartButton
2. Inspector → set:

👉 **Process Mode = Always**

---

# 🎮 STEP 10: Add R Key

Go to:

👉 **Project → Project Settings → Input Map**

1. Add action: `restart`
2. Click **+**
3. Press **R key**

---

# ⚠️ STEP 11: Allow Input When Paused

1. Select **Main node**
2. Set:

👉 **Process Mode = Always**

---

# 🧪 FINAL TEST

Run game:

✔ Move player
✔ Touch coin → disappears
✔ New coin appears
✔ Score increases
✔ At 10 → **YOU WIN**
✔ Restart button visible
✔ Click button → restart
✔ Press **R** → restart

---





Final Scripts: -
main.gd
extends Node2D

var score = 0
var max_score = 10

@onready var score_label = $CanvasLayer/ScoreLabel
@onready var game_over_label = $CanvasLayer/GameOverLabel
@onready var restart_button = $CanvasLayer/RestartButton

var coin_scene = preload("res://coin.tscn")

func _ready():
	randomize()
	update_score()
	connect_all_coins()

func connect_all_coins():
	for coin in get_tree().get_nodes_in_group("coins"):
		coin.connect("collected", Callable(self, "_on_coin_collected"))

func _on_coin_collected(pos):
	score += 1
	update_score()

	# Respawn new coin at random position
	spawn_coin()

	# WIN CONDITION
	if score >= max_score:
		show_game_result("YOU WIN!")

func spawn_coin():
	var coin = coin_scene.instantiate()
	add_child(coin)

	# Random position (adjust range based on your screen)
	coin.position = Vector2(
		randf_range(50, 750),
		randf_range(50, 450)
	)

	coin.add_to_group("coins")
	coin.connect("collected", Callable(self, "_on_coin_collected"))

func update_score():
	score_label.text = "Treasure: " + str(score)

# COMMON GAME END FUNCTION
func show_game_result(text):
	game_over_label.text = text
	game_over_label.visible = true
	restart_button.visible = true
	get_tree().paused = true

# Restart button
func _on_restart_button_pressed():
	get_tree().paused = false
	get_tree().reload_current_scene()

# Press R to restart
func _unhandled_input(event):
	if event.is_action_pressed("restart"):
		get_tree().paused = false
		get_tree().reload_current_scene()




player.gd
extends CharacterBody2D

const SPEED = 200

func _physics_process(delta):
	var direction = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x += 1
	if Input.is_action_pressed("ui_left"):
		direction.x -= 1
	if Input.is_action_pressed("ui_down"):
		direction.y += 1
	if Input.is_action_pressed("ui_up"):
		direction.y -= 1

	velocity = direction.normalized() * SPEED
	move_and_slide()




coin.gd
extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


signal collected

func _on_body_entered(body):
	if body.name == "Player":
		emit_signal("collected", global_position)
		queue_free()
