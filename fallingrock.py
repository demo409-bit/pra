The Falling Rock Dodger
Steps: -
________________________________________
STEP 0: Project Setup
1.	Open Godot Engine
2.	Click New Project
3.	Enter project name: Falling Rock Dodger
4.	Select renderer: Forward+
5.	Click Create & Edit
________________________________________
STEP 1: Create the Rock Scene
1. Create Scene
•	Click New Scene
•	Select Area2D
•	Rename it to Rock
________________________________________
2. Add Sprite
•	Right-click Rock
•	Add Sprite2D
•	Set Texture to icon.svg or a rock image
•	Set Modulate color to Grey
•	Adjust scale if required
________________________________________
3. Add Collision Shape
•	Right-click Rock
•	Add CollisionShape2D
•	Set Shape to New CircleShape2D
•	Resize to match the sprite
________________________________________
4. Rock Script (rock.gd)
Attach this script to Rock:
extends Area2D

@export var fall_speed := 300

func _process(delta):
    position.y += fall_speed * delta

    if position.y > 800:
        queue_free()

func _on_body_entered(body):
    if body.name == "Player":
        get_tree().call_group("game", "game_over")

________________________________________
5. Connect Signal
•	Select Rock
•	Go to Node tab
•	Connect body_entered signal to Rock
•	Save as rock.tscn
________________________________________
STEP 2: Create the Player Scene
1. Create Scene
•	New Scene → CharacterBody2D
•	Rename to Player
________________________________________
2. Add Sprite
•	Add Sprite2D
•	Assign a player image
•	Adjust scale and position
________________________________________
3. Add Collision Shape
•	Add CollisionShape2D
•	Use RectangleShape2D or CapsuleShape2D
•	Resize properly
________________________________________
4. Player Script (player.gd)
Attach this script to Player:
extends CharacterBody2D

@export var SPEED := 400.0

func _physics_process(delta):
    var direction := Input.get_axis("ui_left", "ui_right")

    velocity.x = direction * SPEED
    velocity.y = 0

    move_and_slide()

    position.x = clamp(position.x, 50, 1100)

Save the scene as player.tscn.
________________________________________
STEP 3: Create the Main Game Scene
1. Create Scene
•	New Scene → Node2D
•	Rename to Main
•	Save as main.tscn
________________________________________
2. Add Player
•	Instantiate player.tscn
•	Position the player at the bottom center
________________________________________
3. Add Timers
Add two Timer nodes:
Rock Spawn Timer
•	Name: Timer
•	Wait Time: 0.5
•	Autostart: Enabled
Score Timer
•	Name: ScoreTimer
•	Wait Time: 1
•	Autostart: Enabled
________________________________________
STEP 4: User Interface Setup
1. Add CanvasLayer
•	Add a CanvasLayer node
________________________________________
2. Score Label
•	Add Label
•	Name: ScoreLabel
•	Text: Score: 0
•	Increase font size
•	Position at top-left
________________________________________
3. Game Over Panel
•	Add Panel
•	Name: GameOverPanel
•	Anchor: Full Rect
•	Set background color to semi-transparent black
•	Disable visibility initially
Inside the panel, add:
1.	Label GameOverLabel
•	Text: GAME OVER
•	Large font size
2.	Label FinalScoreLabel
•	Text: Score: 0
3.	Label RestartLabel
•	Text: Press R to Restart
________________________________________
STEP 5: Main Script (main.gd)
Attach this script to Main:
extends Node2D

@export var rock_scene: PackedScene = preload("res://rock.tscn")

var score := 0
var is_game_over := false

func _ready():
    add_to_group("game")
    $Timer.timeout.connect(_on_spawn_timer_timeout)
    $ScoreTimer.timeout.connect(_on_score_timer_timeout)

func _process(delta):
    if is_game_over and Input.is_key_pressed(KEY_R):
        get_tree().reload_current_scene()

func _on_spawn_timer_timeout():
    if is_game_over:
        return

    var rock = rock_scene.instantiate()
    rock.position.x = randf_range(50, 1100)
    rock.position.y = -50
    add_child(rock)

func _on_score_timer_timeout():
    if is_game_over:
        return

    score += 1
    $CanvasLayer/ScoreLabel.text = "Score: " + str(score)

func game_over():
    is_game_over = true
    $Timer.stop()
    $ScoreTimer.stop()

    $CanvasLayer/GameOverPanel.visible = true
    $CanvasLayer/GameOverPanel/FinalScoreLabel.text = "Score: " + str(score)

________________________________________
STEP 6: Final Verification Checklist
•	Player node name is exactly Player
•	Rock uses Area2D
•	Player uses CharacterBody2D
•	Rock uses body_entered signal
•	Both nodes have CollisionShape2D
•	Timer node names match script references
•	GameOverPanel is hidden initially
________________________________________
STEP 7: Game Controls
•	Move Left: Left Arrow / A
•	Move Right: Right Arrow / D
•	Restart Game: R
________________________________________
Conclusion
This project demonstrates:
•	Scene instancing
•	Timers and signals
•	Collision detection
•	Score tracking
•	Game state management
•	Basic UI handling in Godot 4
