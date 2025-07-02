//시도 가능 횟수 설정
const countText = document.getElementById('attempts');
//시도 가능 횟수 초기화
countText.innerHTML = 9;

//input 비우기
const number1 = document.getElementById('number1');
const number2 = document.getElementById('number2');
const number3 = document.getElementById('number3');
number1.value = "";
number2.value = "";
number3.value = "";
//결과창 비우기
const result = document.getElementById('results');
result.innerHTML = "";

//랜덤 숫자 3개 만들기
let randomNumber1 = -1;
let randomNumber2 = -1;
let randomNumber3 = -1;
function setRandomArray() {
    const randomArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    for (let i = randomArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i+1));
        [randomArray[i], randomArray[j]] = [randomArray[j], randomArray[i]];
    }

    randomNumber1 = randomArray[0];
    randomNumber2 = randomArray[1];
    randomNumber3 = randomArray[2];
}
setRandomArray();

function check_numbers() {
    //입력되지 않은 input이 있는지 확인
    if (number1.value == "" || number2.value == "" || number3.value == "") {
        number1.value = "";
        number2.value = "";
        number3.value = "";
        return;
    }

    //입력한 숫자를 확인할 때마다 시도 가능 횟수가 1씩 감소
    countText.innerText = Number(countText.innerText) - 1;

    // 결과 생성 로직
    let strike = 0;
    let ball = 0;
    if (number1.value == randomNumber1) {
        strike += 1;
    }
    else if (number1.value == randomNumber2 || number1.value == randomNumber3) {
        ball += 1;
    }
    if (number2.value == randomNumber2) {
        strike += 1;
    }
    else if (number2.value == randomNumber1 || number2.value == randomNumber3) {
        ball += 1;
    }
    if (number3.value == randomNumber3) {
        strike += 1;
    }
    else if (number3.value == randomNumber1 || number3.value == randomNumber2) {
        ball += 1;
    }

    //결과 출력
    const results = document.getElementById("results");
    results.style.width = "100%";
    
    const newDiv = document.createElement("div");
    newDiv.className="check-result";
    
    if (strike == 0 && ball == 0) {
        newDiv.innerHTML = `
            <div class="left">${number1.value}${number2.value}${number3.value}</div>
            <div class="center">:</div>
            <div class="right">
                <div class="out num-result">O</div>
            </div>
        `;
    }
    else {
        newDiv.innerHTML = `
            <div class="left">${number1.value}${number2.value}${number3.value}</div>
            <div class="center">:</div>
            <div class="right">
                ${strike}<div class="strike num-result">S</div>${ball}<div class="ball num-result">B</div>
            </div>
        `;
        
    }
    document.getElementById("results").appendChild(newDiv);
    //게임이 끝났는지 확인하고 결과 이미지 출력
    if (countText.innerText == 0 || strike == 3) {
        if (strike == 3) {
            document.getElementById("game-result-img").src = "./success.png";
        }
        else {
            document.getElementById("game-result-img").src = "./fail.png";
        }
        // 확인하기 버튼 비활성화하기
        const submitBtn = document.querySelector('.submit-button');
        submitBtn.disabled = true;
    }
}


