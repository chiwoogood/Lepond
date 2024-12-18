const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
});

document.addEventListener('DOMContentLoaded', function() {
    const wrapper = document.querySelector('#barba-wrapper');
    console.log('Wrapper found:', wrapper); // 디버깅용 로그

    if (wrapper) {
        barba.init({
            transitions: [{
                name: 'fade',
                leave(data) {
                    console.log('Leaving:', data.current.container); // 디버깅 로그
                    return gsap.to(data.current.container, { opacity: 0 });
                },
                enter(data) {
                    console.log('Entering:', data.next.container); // 디버깅 로그
                    return gsap.from(data.next.container, { opacity: 0 });
                }
            }]
        });
    } else {
        console.error('No Barba wrapper found in the DOM.');
    }
});
