document.addEventListener('DOMContentLoaded', function () {
  // header scroll state
  const header = document.getElementById('siteHeader');
  if (header) {
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
    window.addEventListener('scroll', onScroll);
    onScroll();
  }

  // animated counters
  const counters = document.querySelectorAll('[data-count]');
  counters.forEach(el => {
    const target = parseInt(el.getAttribute('data-count'), 10);
    let cur = 0;
    const step = Math.max(1, Math.round(target / 40));
    const t = setInterval(() => {
      cur += step;
      if (cur >= target) { cur = target; clearInterval(t); }
      el.textContent = cur;
    }, 30);
  });

  // reveal on scroll
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: .15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  // pillars accordion
  document.querySelectorAll('.pillar-head').forEach(head => {
    head.addEventListener('click', () => {
      const pillar = head.parentElement;
      const wasOpen = pillar.classList.contains('open');
      document.querySelectorAll('.pillar').forEach(p => p.classList.remove('open'));
      if (!wasOpen) pillar.classList.add('open');
    });
  });

  // mobile menu
  const toggle = document.querySelector('.menu-toggle');
  const navlinks = document.querySelector('.navlinks');
  if (toggle && navlinks) {
    toggle.addEventListener('click', () => {
      const isOpen = navlinks.style.display === 'flex';
      if (isOpen) {
        navlinks.style.display = '';
        navlinks.removeAttribute('style');
      } else {
        navlinks.style.cssText = 'display:flex;position:fixed;top:70px;left:20px;right:20px;background:#fff;flex-direction:column;padding:20px;border-radius:16px;box-shadow:0 20px 50px rgba(10,50,90,.2);gap:18px;z-index:200;';
        navlinks.querySelectorAll('a').forEach(a => a.style.color = '#132436');
      }
    });
  }
});
