Jumping Game

GAME FEATURES (What we are building)
Player with left / right movement
Double jump
Solid platforms
Coins that can be collected
Score UI
Win message
Death zone (fall → restart)
Restart key
________________________________________
🔹 PART 0: PROJECT SETUP
Step 0.1: Create Project
1.	Open Godot
2.	Click New Project
3.	Name it: JumpingGame
4.	Choose an empty folder
5.	Renderer: Forward+
6.	Click Create & Edit
________________________________________
🔹 PART 1: CREATE MAIN SCENE
Step 1.1: New Scene
1.	Top menu → Scene
2.	Click New Scene
3.	Choose 2D Scene
Step 1.2: Rename Root Node
•	Rename Node2D → Main
Step 1.3: Save Scene
1.	Press Ctrl + S
2.	Name: Main.tscn
3.	Save inside a folder (example: scenes/)
________________________________________
🔹 PART 2: CREATE PLAYER (JUMPER)
🧍 Create Jumper Scene
Step 2.1: New Scene
1.	Scene → New Scene
2.	Choose 2D Scene
3.	Delete Node2D
Step 2.2: Add CharacterBody2D
1.	Click +
2.	Add CharacterBody2D
3.	Rename to Jumper
________________________________________
Step 2.3: Add Sprite
1.	Select Jumper
2.	Click +
3.	Add Sprite2D
4.	Inspector → Texture → load icon.svg
________________________________________
Step 2.4: Add Collision
1.	Select Jumper
2.	Click +
3.	Add CollisionShape2D
4.	Inspector → Shape → New RectangleShape2D
5.	Resize rectangle to cover sprite
________________________________________
Step 2.5: Attach Script to Jumper
1.	Select Jumper
2.	Click 📜➕ Attach Script
3.	Click Create
4.	Paste this:
extends CharacterBody2D

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

var jump_count = 0
var max_jumps = 2

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta):
	if not is_on_floor():
		velocity.y += gravity * delta

    else:
		jump_count = 0

    if Input.is_action_just_pressed("ui_up") and jump_count<max_jumps:
		velocity.y = JUMP_VELOCITY

        jump_count += 1

    var direction = Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * SPEED

    else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

    move_and_slide()

________________________________________
Step 2.6: Save Jumper Scene
•	Ctrl + S
•	Name: Jumper.tscn
________________________________________
🔹 PART 3: ADD JUMPER TO MAIN
1.	Open Main.tscn
2.	Select Main
3.	Click Instantiate Child Scene (🔗)
4.	Select Jumper.tscn
5.	Position Jumper in scene
________________________________________
🔹 PART 4: ADD PLATFORMS (GROUND)
Step 4.1: Add Ground
1.	Select Main
2.	Click +
3.	Add StaticBody2D
4.	Rename to Ground
________________________________________
Step 4.2: Ground Visual
1.	Select Ground
2.	Click +
3.	Add Sprite2D
4.	Assign icon.svg
5.	Scale X = 10, Y = 0.5
________________________________________
Step 4.3: Ground Collision
1.	Select Ground
2.	Click +
3.	Add CollisionShape2D
4.	Shape → RectangleShape2D
5.	Resize to match sprite
________________________________________
Step 4.4: Duplicate Platforms
•	Select Ground
•	Ctrl + D
•	Move copies to create jumping platforms
________________________________________
🔹 PART 5: CREATE COIN SCENE
🪙 Coin Scene
Step 5.1: New Scene
1.	Scene → New Scene
2.	Choose 2D Scene
3.	Delete Node2D
________________________________________
Step 5.2: Add Area2D
1.	Click +
2.	Add Area2D
3.	Rename to Coin
________________________________________
Step 5.3: Coin Visual
1.	Select Coin
2.	Add Sprite2D
3.	Assign coin.svg
________________________________________
Step 5.4: Coin Collision
1.	Select Coin
2.	Add CollisionShape2D
3.	Shape → CircleShape2D
4.	Resize to cover coin
________________________________________
Step 5.5: Coin Script
Attach script to Coin and paste:
Just add this code in the script don’t delete the whole script and add
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Tab;

extends Area2D

func _on_body_entered(body):
	if body.name == "Jumper":
		get_tree().current_scene.update_score()

        queue_free()
________________________________________
Step 5.6: Connect Signal
1.	Select Coin
2.	Node tab → double-click body_entered
3.	Select Coin
4.	Click Connect
________________________________________
Step 5.7: Save Coin Scene
•	Ctrl + S
•	Name: Coin.tscn
________________________________________
🔹 PART 6: ADD COINS TO MAIN
1.	Open Main.tscn
2.	Instantiate Coin.tscn
3.	Duplicate to make 3 coins
4.	Place above platforms
________________________________________
🔹 PART 7: HUD (UI)
Step 7.1: CanvasLayer
1.	Select Main
2.	Add CanvasLayer
3.	Rename to HUD
________________________________________
Step 7.2: Score Label
1.	HUD → Add Label
2.	Rename → ScoreLabel
3.	Text → Coins: 0
4.	Position top-left
________________________________________
Step 7.3: Win Label
1.	HUD → Add Label
2.	Rename → WinLabel
3.	Text → YOU WIN!
4.	Font Size → 50
5.	Center screen
6.	Inspector → Visibility → ❌ Visible
7.	To increase the font size search font size its under theme overrides
________________________________________
🔹 PART 8: MAIN SCRIPT (GAME LOGIC)
Attach script to Main:
using System;
using System.Windows.Forms;

extends Node2D

var score = 0
var total_coins = 3

func _ready():
	$HUD / WinLabel.hide()

func update_score():
	score += 1
	$HUD / ScoreLabel.text = "Coins: " + str(score)

    if score >= total_coins:
		win_game()

func win_game():
	$HUD / WinLabel.show()
	$Jumper.set_physics_process(false)

func _input(event):
	if event.is_action_pressed("ui_text_submit"):
		get_tree().reload_current_scene()
________________________________________
🔹 PART 9: DEATH ZONE
Step 9.1: Add DeathZone
1.	Main → Add Area2D
2.	Rename → DeathZone
________________________________________
Step 9.2: Collision
1.	Add CollisionShape2D
2.	Shape → WorldBoundaryShape2D
3.	Place below platforms
________________________________________
Step 9.3: Signal
1.	Select DeathZone
2.	Node tab → body_entered
3.	Connect to Main
func _on_death_zone_body_entered(body):
	if body.name == "Jumper":
		get_tree().reload_current_scene()
________________________________________
🔹 PART 10: SET MAIN SCENE
1.	Project → Project Settings
2.	Application → Run
3.	Main Scene → select Main.tscn
________________________________________
🔹 PART 11: DEBUG CHECK (IMPORTANT)
While running:
•	Debug → Visible Collision Shapes
•	Blue shapes must appear on:
•	Player
•	Ground
•	Coins
________________________________________


# 🔴 STEP 1: ADD UI (HUD)

In your **Main scene**:

### 1. Add Game Over Label

* Select `HUD`
* Add → **Label**
* Rename → `GameOverLabel`
* Text → `GAME OVER`
* Increase font size (Theme Overrides → Font Size = 40–60)
* Center it on screen
* ❌ Uncheck **Visible**



### 2. Add Restart Button

* Select `HUD`
* Add → **Button**
* Rename → `RestartButton`
* Text → `Restart`
* Place below GameOverLabel
* ❌ Uncheck **Visible**



# 🔴 STEP 2: UPDATE MAIN SCRIPT

Attach this to your `Main` scene:
Change the Whole script to this:
extends Node2D

var score = 0
var total_coins = 3
var game_over = false

func _ready():
	$HUD/GameOverLabel.hide()
	$HUD/RestartButton.hide()

func update_score():
	score += 1
	$HUD/ScoreLabel.text = "Coins: " + str(score)

	if score >= total_coins:
		win_game()

func win_game():
	$HUD/WinLabel.show()
	$Jumper.set_physics_process(false)

# 🔥 GAME OVER FUNCTION
func game_over_func():
	game_over = true
	$HUD/GameOverLabel.show()
	$HUD/RestartButton.show()
	$Jumper.set_physics_process(false)

# 🔥 BUTTON CLICK
func _on_restart_button_pressed():
	get_tree().reload_current_scene()

# 🔥 KEY PRESS (R)
func _input(event):
	if event.is_action_pressed("ui_text_submit") or event.is_action_pressed("ui_accept"):
		get_tree().reload_current_scene()

	if event.is_action_pressed("ui_cancel"): # optional
		get_tree().reload_current_scene()

	if event is InputEventKey and event.pressed:
		if event.keycode == KEY_R:
			get_tree().reload_current_scene()


func _on_death_zone_body_entered(body):
	if body.name == "Jumper":
		game_over_func()



---

#  STEP 3: CONNECT BUTTON

1. Select `RestartButton`
2. Go to **Node tab**
3. Double click `pressed()`
4. Connect to `Main`
5. It will create:

func _on_restart_button_pressed():




#  STEP 4: MODIFY DEATH ZONE

Update your death zone function:

func _on_death_zone_body_entered(body):
	if body.name == "Jumper":
		game_over_func()








#All Scripts:
#Main.gd
extends Node2D

var score = 0
var total_coins = 3
var game_over = false

func _ready():
	$HUD/GameOverLabel.hide()
	$HUD/RestartButton.hide()

func update_score():
	score += 1
	$HUD/ScoreLabel.text = "Coins: " + str(score)

	if score >= total_coins:
		win_game()

func win_game():
	$HUD/WinLabel.show()
	$Jumper.set_physics_process(false)

# 🔥 GAME OVER FUNCTION
func game_over_func():
	game_over = true
	$HUD/GameOverLabel.show()
	$HUD/RestartButton.show()
	$Jumper.set_physics_process(false)

# 🔥 BUTTON CLICK
func _on_restart_button_pressed():
	get_tree().reload_current_scene()

# 🔥 KEY PRESS (R)
func _input(event):
	if event.is_action_pressed("ui_text_submit") or event.is_action_pressed("ui_accept"):
		get_tree().reload_current_scene()

	if event.is_action_pressed("ui_cancel"): # optional
		get_tree().reload_current_scene()

	if event is InputEventKey and event.pressed:
		if event.keycode == KEY_R:
			get_tree().reload_current_scene()


func _on_death_zone_body_entered(body):
	if body.name == "Jumper":
		game_over_func()







#jumper.gd
extends CharacterBody2D

const SPEED = 300.0
const JUMP_VELOCITY = -400.0

# VARIABLES FOR DOUBLE JUMP
var jump_count = 0
var max_jumps = 2

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta):
	# Add gravity.
	if not is_on_floor():
		velocity.y += gravity * delta
	else:
		# Reset jumps when you touch the floor
		jump_count = 0

	# Handle Jump (Double Jump)
	if Input.is_action_just_pressed("ui_up") and jump_count < max_jumps:
		velocity.y = JUMP_VELOCITY
		jump_count += 1

	# Horizontal Movement
	var direction = Input.get_axis("ui_left", "ui_right")
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

	move_and_slide()








#coin.gd
extends Area2D

func _on_body_entered(body):
	if body.name == "Jumper":
		get_tree().current_scene.update_score()
		queue_free()
