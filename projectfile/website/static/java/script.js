const filling = document.querySelector('.filling')
const loginlink = document.querySelector('.login-link')
const registerlink = document.querySelector('.register-link');

registerlink.addEventListener('click',()=> {
    filling.classList.add('active');
});

loginlink.addEventListener('click',()=> {
    filling.classList.remove('active');
});


