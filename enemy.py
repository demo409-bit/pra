Enemy Game

2D Dodge Game Using Godot 4
________________________________________
1. Project Setup
1.	Open Godot Engine (version 4.x).
2.	Click New Project.
3.	Give the project a name (example: DodgeGame).
4.	Choose a folder location.
5.	Select Renderer: Forward+.
6.	Click Create & Edit.
________________________________________

2. Creating the Player Scene
2.1 Scene Creation
1.	Create a new scene.
2.	Select Area2D as the root node.
3.	Rename it to Player.

2.2 Add Child Nodes
1.	Add a Sprite2D node.
•	Assign icon.svg as the texture.
•	Set Self Modulate color to blue.
2.	Add a CollisionShape2D node.
•	Set Shape to RectangleShape2D.
•	Resize to cover the sprite.

2.3 Player Movement Script (player.gd)
Attach the following script to Player:
extends Area2D

@export var speed = 400

func _process(delta):
	if get_tree().paused:
		return

    var velocity = Vector2.ZERO

    if Input.is_action_pressed("ui_right"):
		velocity.x += 1

    if Input.is_action_pressed("ui_left"):
		velocity.x -= 1

    if Input.is_action_pressed("ui_down"):
		velocity.y += 1

    if Input.is_action_pressed("ui_up"):
		velocity.y -= 1

    if velocity != Vector2.ZERO:
		velocity = velocity.normalized()

    position += velocity * speed * delta

    var screen_size = get_viewport_rect().size
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)


4.	Save the scene as player.tscn.
________________________________________

3. Creating the Enemy Scene
3.1 Scene Creation
1.	Create a new scene.
2.	Root node: Area2D
3.	Rename it to Enemy.

3.2 Add Child Nodes
1.	Add Sprite2D.
•	Use icon.svg.
•	Set Self Modulate color to red.
2.	Add CollisionShape2D.
•	RectangleShape2D covering the sprite.

3.3 Enemy Script (enemy.gd)

extends Area2D

@export var speed = 200
var direction = 1

func _process(delta):
	position.x += speed * direction * delta

    if position.x > 1000 or position.x < 50:
		direction *= -1

func _on_area_entered(area):
	if area.name == "Player":
		get_parent().end_game()



4.	Connect area_entered signal to the Enemy node.
5.	Save as Enemy.tscn.
________________________________________

4. Creating the Goal Scene

4.1 Scene Setup
1.	Create a new scene.
2.	Root node: Area2D
3.	Rename it to Goal.

4.2 Add Child Nodes
1.	Sprite2D using icon.svg.
•	Set Self Modulate color to green.
2.	CollisionShape2D with RectangleShape2D.

4.3 Goal Script (goal.gd)
extends Area2D

func _on_area_entered(area):
	if area.name == "Player":
		get_parent().add_score()

        var screen_size = get_viewport_rect().size
		position.x = randi_range(200, screen_size.x - 200)
		position.y = randi_range(100, screen_size.y - 100)
4.	Connect area_entered signal.
5.	Save as goal.tscn.
________________________________________

5. Creating the Main Scene

5.1 Scene Setup
1.	Create a new scene. > Select 2d Scene.
2.	Root node: Node2D
3.	Rename it to Main.

5.2 Add Game Elements
1.	Instantiate:
•	Player
•	Goal
•	3–4 Enemy scenes
2.	Position:
•	Player on left side
•	Goal on right side
•	Enemies between them
________________________________________

6. User Interface (UI)
Select Main and add the following UI elements:
6.1 CanvasLayer
1.	Add CanvasLayer to Main.

6.2 Instruction Label
1.	Add Label under CanvasLayer.
2.	Text:
3.	Dodge the Red Boxes to reach the Green Goal!
4.	Place at the top center.

6.3 Score Label
1.	Add another Label.
2.	Rename it to ScoreLabel.
3.	Text:
4.	Score: 0
5.	Place at top-left.

6.4 Game Over Label
1.	Add another Label.
2.	Rename it to GameOverLabel.
3.	Text:
4.	GAME OVER
5.	Press R to Restart
6.	Center it.
7.	Set Visible to false. (Inspector → Visible = untick )

Add a Win Label in UI (same way you added GameOverLabel):

👉 In CanvasLayer

Add Label → rename to WinLabel
Text:
YOU WIN!
Press R to Restart

Set Visible = false (In Inspector → Visibility > Visible = untick)
________________________________________
7. Main Game Logic Script (main.gd)
Attach this script to Main:

extends Node2D

var score = 0
var game_over = false

@onready var score_label = $CanvasLayer/ScoreLabel
@onready var game_over_label = $CanvasLayer/GameOverLabel

func _ready():
	score_label.text = "Score: 0"

    game_over_label.visible = false

func add_score():
	if game_over:
		return
    score += 1

    score_label.text = "Score: " + str(score)

func end_game():
	if game_over:
		return
    game_over = true

    game_over_label.visible = true

    get_tree().paused = true

func _input(event):
	if game_over and event.is_action_pressed("restart"):
		get_tree().paused = false
		get_tree().reload_current_scene()
________________________________________

8. Input Map Configuration
1.	Go to Project → Project Settings → Input Map.
2.	Add a new action named:
3.	restart
4.	Assign key R to it.
________________________________________

9. Pause Mode Configuration (Critical Step)
1.	Select Main (Node2D).
2.	Inspector → Process.
3.	Set Mode = Always.
This allows the restart key to work while the game is paused.
________________________________________




Final Scripts: 
main.gd

extends Node2D

var score = 0
var game_over = false

@onready var score_label = $CanvasLayer/ScoreLabel
@onready var game_over_label = $CanvasLayer/GameOverLabel

func _ready():
	score_label.text = "Score: 0"

	game_over_label.visible = false
	win_label.visible = false
	
	
func add_score():
	if game_over:
		return

	score += 1
	score_label.text = "Score: " + str(score)

	if score >= win_score:
		win_game()
		
func win_game():
	game_over = true
	win_label.visible = true
	get_tree().paused = true

func end_game():
	if game_over:
		return
	game_over = true

	game_over_label.visible = true

	get_tree().paused = true

func _input(event):
	if game_over and event.is_action_pressed("restart"):
		get_tree().paused = false
		get_tree().reload_current_scene()


var win_score = 5

@onready var win_label = $CanvasLayer/WinLabel





player.gd 
extends Area2D

@export var speed = 400

func _process(delta):
	if get_tree().paused:
		return

	var velocity = Vector2.ZERO

	if Input.is_action_pressed("ui_right"):
		velocity.x += 1

	if Input.is_action_pressed("ui_left"):
		velocity.x -= 1

	if Input.is_action_pressed("ui_down"):
		velocity.y += 1

	if Input.is_action_pressed("ui_up"):
		velocity.y -= 1

	if velocity != Vector2.ZERO:
		velocity = velocity.normalized()

	position += velocity * speed * delta

	var screen_size = get_viewport_rect().size
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)





enemy.gd 

extends Area2D

@export var speed = 200
var direction = 1

func _process(delta):
	position.x += speed * direction * delta

	if position.x > 1000 or position.x < 50:
		direction *= -1

func _on_area_entered(area):
	if area.name == "Player":
		get_parent().end_game()






goal.gd
extends Area2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_area_entered(area):
	if area.name == "Player":
		get_parent().add_score()

		var screen_size = get_viewport_rect().size
		position.x = randi_range(200, screen_size.x - 200)
		position.y = randi_range(100, screen_size.y - 100)
