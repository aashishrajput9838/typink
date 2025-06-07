import * as robot from 'robotjs';

// Function to simulate typing text
function typeText(text: string, delay: number = 100): void {
    const lines = text.split('\n');
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        robot.typeString(line);
        robot.setKeyboardDelay(delay);
        
        if (i < lines.length - 1) {
            robot.keyTap('enter');
            robot.setKeyboardDelay(delay);
        }
    }
}

// Function to start auto-typing
function startAutoTyping(): void {
    console.log('Auto-typing will start in 5 seconds...');
    console.log('Please place your cursor where you want the text to be typed.');
    
    // Wait for 5 seconds before starting
    setTimeout(() => {
        const textToType = `def example_function():
    # This is an indented comment
    if True:
        print("This is indented code")
        for i in range(5):
            print(f"Number: {i}")
    
    return "Done"`;
        
        console.log('Starting to type...');
        typeText(textToType);
        console.log('Finished typing!');
    }, 5000);
}

// Start the program
console.log('Auto-typing program started.');
console.log('Press Ctrl+C to exit.');
startAutoTyping(); 