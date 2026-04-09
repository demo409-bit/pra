STEP 1: Create Main Scene
Click 2D Scene
Rename root node:
Main
Save scene:
Main.tscn

STEP 2: Create Player
-Add Player Node
Select Main
Click + (Add Child Node)
Search: Area2D
Click Create
Rename:
Player
-Add Sprite
Select Player
Click +
Add → Sprite2D

In Inspector:
Texture → drag icon.svg

-Add Collision
Select Player
Click +
Add → CollisionShape2D

-In Inspector:
Shape → New RectangleShape2D
Resize it to cover player

-Add Player Script
Select Player
Click Attach Script
Click Create

extends Area2D
@export var speed = 400
func _process(delta):
	var velocity = Vector2.ZERO	
	if Input.is_action_pressed("ui_right"):
		velocity.x += 1
	if Input.is_action_pressed("ui_left"):
		velocity.x -= 1
	if Input.is_action_pressed("ui_down"):
		velocity.y += 1
	if Input.is_action_pressed("ui_up"):
		velocity.y -= 1
	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
	position += velocity * delta

STEP 3:Create Coin Scene
-New Scene
3.1 Add Coin Node
Click +
Add → Area2D
Rename:
Coin

3.2 Add Sprite
Select Coin
Add → Sprite2D
Texture → icon.svg
Make yellow:
Inspector → Self Modulate → Yellow

3.3 Add Collision
Select Coin
Add → CollisionShape2D
Shape → CircleShape2D

3.4 Add Script
Select Coin
Attach Script → Create

extends Area2D
signal coin_collected
func _ready():
	randomize()
func _on_area_entered(area):
	emit_signal("coin_collected")
	respawn()
func respawn():
	position.x = randf_range(50, 1100)
	position.y = randf_range(50, 600)
	
3.5 Connect Signal (IMPORTANT)
Select Coin
Go to Node tab (right side)
Double-click:
area_entered(area: Area2D)
Click Connect

-Save Scene

STEP 4: Add Coin to Main Scene
Go back to Main tab
Click Instantiate Child Scene (chain icon)
Select:
Coin.tscn
Main
├── Player
├── Coin

STEP 5: Create UI (Score + Button)
5.1 Add HUD
Select Main
Add → CanvasLayer
Rename: HUD

5.2 Add Score Label
Select HUD
Add → Label
Rename:
ScoreLabel
Inspector → Text:
Score: 0

6.1 Add Restart Button
Select HUD
Add → Button
Rename:
RestartButton
Text:Restart

STEP 7: Main Script
7.1 Attach Script
Select Main
Click Attach Script → Create

extends Node2D
var score := 0
@onready var score_label = $HUD/ScoreLabel
@onready var coin = $Coin
func _ready():
	update_score()
	coin.connect("coin_collected", Callable(self, "_on_coin_collected"))
func update_score():
	score_label.text = "Score: " + str(score)
func add_score():
	score += 1
	update_score()
func _on_coin_collected():
	add_score()
func _process(delta):
	if Input.is_action_just_pressed("restart"):
		restart_game()
func restart_game():
	score = 0
	update_score()
	coin.position = Vector2(300, 200)
func _on_restart_button_pressed():
	restart_game()
	
STEP 8: Connect Restart Button
Select RestartButton
Go to Node tab
Double-click: pressed()
Connect to Main

STEP 9: Add R Key (IMPORTANT)
Go to:Project → Project Settings → Input Map
Add:
Action: restart
Key: R
