const canvas = document.querySelector(".canvas");
//console.log(canvas);
const ctx = canvas.getContext("2d");
//console.log(ctx);
const scale = 10;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

var snake;
var gameSpeed = 250;

(function setup() {
    snake = new Snake();
    fruit = new Fruit();
    fruit.pickLocation();
    // console.log(fruit);

    function drawsUpdates() {
        ctx.clearRect(0,0,canvas.width, canvas.height)
        fruit.draw();
        snake.update();
        snake.draw();

        if( snake.eat(fruit)){
            // console.log("EATING");
            fruit.pickLocation();
        }
    }

    window.setInterval( drawsUpdates, gameSpeed);
    
}());

window.addEventListener('keydown', function(event) {
    // console.log(event);
    const direction = event.key.replace('Arrow','');
    // console.log(direction)
    snake.changeDirection(direction);
});