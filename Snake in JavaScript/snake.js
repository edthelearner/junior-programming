function Snake() {
    this.x = 0;
    this.y = 0;
    this.xSpeed = scale * 1;
    this.ySpeed = scale * 0;
    this.total = 0;
    this.tail = [];
    console.log(this.tail);

    this.draw = function() {
        ctx.fillStyle = "#FFFFFF";
        for( let i = 0; i < this.tail.length; i++) {
            ctx.fillRect(this.tail[i].x, this.tail[i].y, scale, scale);
        }

        ctx.fillRect(this.x, this.y, scale, scale);
    }

    this.update = function() {
        
        // this for loop 'moves' the tail along.
        // can you see how?
        for(let i = 0; i < this.tail.length - 1; i++ ) {
            this.tail[i] = this.tail[i+1];    
        }
        
        // assigns the last index of the tail to the current position
        // note that this is one freaky deeky snake
        // the 'end' of it's tail is technically next to the head
        this.tail[this.total - 1] = { x: this.x, y: this.y };     
        

        this.x += this.xSpeed;
        this.y += this.ySpeed;

        if( this.x > canvas.width ) {
            // if it goes off to the right start it again at the left
            this.x = 0;
        }
        if( this.x < 0 ) {
            // if it goes off to the left start it again at the right
            this.x = canvas.width;
        }
        if( this.y > canvas.height ) {
            // if it goes off to the bottom start it again at the top
            this.y = 0;
        }
        if( this.y < 0 ) {
            // if it goes off to the top start it again at the bottom
            this.y = canvas.height;
        }
    }

    this.changeDirection = function(direction) {
        if( direction == 'Up' ){
            this.xSpeed = 0;
            this.ySpeed = scale * -1;
        }
        else if( direction == 'Down'){
            this.xSpeed = 0;
            this.ySpeed = scale * 1;
        }
        else if( direction == 'Right'){
            this.xSpeed = scale * 1;
            this.ySpeed = 0;
        }
        else if( direction == 'Left'){
            this.xSpeed = scale * -1;
            this.ySpeed = 0;
        }
    }

    this.eat = function(fruit) {
        // console.log(fruit);
        if( this.x === fruit.x && this.y === fruit.y){
            this.total++;
            // console.log(this.tail);
            return true;
        }

        return false;
    }
}