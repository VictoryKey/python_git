document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (username === '' || password === '') {
            event.preventDefault();
            const message = document.querySelector('.message');
            message.textContent = '用户名和密码不能为空！';
        }
    });
});
