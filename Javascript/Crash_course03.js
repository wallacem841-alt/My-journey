//try catch/user input
//user input
let weight_input;
let height_input;

//button press
document.getElementById('mysubmit').onclick = function(){
    weight_input = document.getElementById('input_weight').value;
    height_input = document.getElementById('input_height').value;
    weight = Number(weight_input);
    height = Number(height_input) / 100;

    //check if either weight or height is NaN
    if (isNaN(weight) || isNaN(height)) {
        document.getElementById('Result').textContent = "Error: Not a number, dummy!";
        return; // Stop execution
    }

    //Calculates BMI
    let bmi = weight / (height**2);

    //Outputs BMI
    switch (true){
        case (bmi < 16 && bmi >= 0):
            document.getElementById('Result').textContent = 'Result: Severe Thinness, You better go around with some weights or you gon go flying';
            break;
        case (bmi == 16):
            document.getElementById('Result').textContent = 'Result: Moderate Thinness, fuuu! did you went flying?';
            break;
        case (bmi > 16 && bmi <= 18.5):
            document.getElementById('Result').textContent = 'Result: Mild Thinness, better hold onto something or you might blow away!';
            break;
        case (bmi > 18.5 && bmi <= 25):
            document.getElementById('Result').textContent = 'Result: Normal, enjoy it while it lasts, you doornob';
            break;
        case (bmi > 25 && bmi <= 30):
            document.getElementById('Result').textContent = 'Result: Overweight, time to back away from the buffet! Slowly fatso';
            break;
        case (bmi > 30 && bmi <= 35):
            document.getElementById('Result').textContent = "Result: Obese Class I, the scale called and said 'one at a time, please!'";
            break;
        case (bmi > 35 && bmi <= 40):
            document.getElementById('Result').textContent = "Result: Obese Class II, when's the last time you saw your toes?";
            break;
        case (bmi > 40):
            document.getElementById('Result').textContent = "Result: Obese Class III, My 600-lb Life called, they've found their next contendent";
            break;
        default:
            document.getElementById('Result').textContent = "Result: you've put a negative number didn't you? dum dum"
    }
}