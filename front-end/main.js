let saladWrapper = document.querySelector('.salad__wrapper')
let cartCards = document.querySelector('.cart__cards');
let cartButton = document.querySelector('.cart-button')
let cart = document.querySelector('.cart');

let auth = document.querySelector('.auth');
let reg = document.querySelector('.reg');

let authBtn = document.querySelector('.authBtn');
let regBtn = document.querySelector('.regBtn');

let authClose = document.querySelector('.authClose');
let regClose = document.querySelector('.regClose');

let body = document.body

let eatProduct = document.querySelectorAll('.eat__product')
let productInfo = document.



// представления 
let products = [
//   {
//     id: 1,
//     img: "http://127.0.0.1:8000/media/product/pexels-nishant-aneja-2955820.jpg",
//     name: "Жаренные Сордельки",
//     weight: 50,
//     price: "150",
//     desc: "Сардельки, горошек, зелень",
//     calorie: 12,
//     protein: 34,
//     carbohydrate: 1,
//     fat: 16,
//     type: "hot",
//     recalls: [
//       {
//         user: "kirill22",
//         name: "Кирилл Проскурин",
//         overall_rating: 5,
//         speed_grade: true,
//         taste_grade: true,
//         comment: "Вкусные сардельки",
//       },
//       {
//         user: "igore",
//         overall_rating: 1,
//         speed_grade: true,
//         taste_grade: false,
//         comment: "Вкусно и дешево",
//       },
//     ],
//   },
];

let basket = [];


let productsList = products.map((product) => {
    let div = document.createElement('div')
    div.classList.add('eat__product')
    div.innerHTML= `
    <img src="img/salad.png" alt="">
    <h3>${product.name}</h3>
    <p>${product.desc}</p>
    <div class="new__card-footer">
        <div class="price">
            <h4>${product.price}₽</h4>
            <p>${product.weight}г</p>
        </div>
        <button data-id=${product.id} class="add__cart">+</button>
    </div>
    `
    saladWrapper.prepend(div)
})






saladWrapper.addEventListener('click', event => {
    if (event.target.classList.contains('add__cart')) {
        console.log('click');
        if(event.target.matches('[data-id]')){
            let id = event.target.getAttribute('data-id');
            let basketEl = {
                name: products[id-1].name,
                price: products[id-1].price,
            }

            basket.push(basketEl)
            console.log(basket);
        }
    }
}) 

let basketList = basket.map((basketEl) => {
    let div = document.createElement("div")
    div.classList.add('.cart__cards-el')
    div.innerHTML = `
        <div class="cart__cards-el">
        <div class="cart__cards-el-img">
            <img src="img/salad.png" alt="">
        </div>
        <div class="cart__cards-el-text">
            <h2>${basketEl.name}</h2>
            <h3>${basketEl.price}₽</h3>
        </div>
        <div class="cart__cards-el-del">
            <img src="img/trash.svg" alt="">
        </div>
    </div>
    `

    cartCards.prepend(div)
})


cartButton.addEventListener("click", () => {
    cart.style.display = 'block'
    body.style.overflow = 'hidden'
})

authBtn.addEventListener("click", () => {
    auth.style.display = "block"
    body.style.overflow = 'hidden'
})

regClose.addEventListener("click", ()=> {
    reg.style.display = "none"
    body.style.overflow = 'hidden'
})



regClose.addEventListener("click", () => {
    reg.style.display = "block"
    body.style.overflowY = 'scroll'
})

authClose.addEventListener("click", ()=> {
    auth.style.display = "none"
    body.style.overflowY = 'scroll'
})


eatProduct.forEach((el) => {
    el.addEventListener("click", () => {

    })
})



