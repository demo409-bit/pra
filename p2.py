'''
<!DOCTYPE html>
<html>
<head>
    <title>Easy 2D Transformations</title>
    <style>
        body { background: #222; text-align: center; color: white; font-family: sans-serif; }
        canvas { border: 2px solid white; background: #000; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Use Arrows (Move), A/D (Rotate), W/S (Scale)</h2>
    <canvas id="gameCanvas" width="500" height="400"></canvas>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        // 1. Initial State
        let x = 250, y = 200, angle = 0, scale = 1;
        const speed = 4, playerSize = 40, keys = {};

        // 2. Track Keys
        window.onkeydown = (e) => keys[e.key] = true;
        window.onkeyup = (e) => keys[e.key] = false;

        function update() {
            // Translation (Move)
            if (keys["ArrowUp"])    y -= speed;
            if (keys["ArrowDown"])  y += speed;
            if (keys["ArrowLeft"])  x -= speed;
            if (keys["ArrowRight"]) x += speed;

            // Rotation (Rotate)
            if (keys["a"]) angle -= 0.05;
            if (keys["d"]) angle += 0.05;

            // Scaling (Size)
            if (keys["w"]) scale += 0.02;
            if (keys["s"]) scale = Math.max(0.2, scale - 0.02); // Prevents disappearing
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear screen

            ctx.save();            // Save normal state
            ctx.translate(x, y);   // Move coordinate system to (x, y)
            ctx.rotate(angle);     // Spin coordinate system
            ctx.scale(scale, scale); // Stretch coordinate system

            // Draw square at (0,0) because translate moved the "center" for us
            ctx.fillStyle = "cyan";
            ctx.fillRect(-playerSize/2, -playerSize/2, playerSize, playerSize);
           
            ctx.restore();         // Reset state for next frame
           
            update();
            requestAnimationFrame(draw);
        }

        draw(); // Start the game
    </script>
</body>
</html>
'''
