(function(){
  'use strict';
  function initNav(){
    document.querySelectorAll('.aq-header').forEach(function(header){
      var btn=header.querySelector('.aq-menu-btn');
      var menu=header.querySelector('.aq-mobile-menu');
      if(!btn || !menu || btn.dataset.navReady==='1') return;
      btn.dataset.navReady='1';
      function close(){
        menu.classList.remove('aq-menu-open');
        btn.setAttribute('aria-expanded','false');
        btn.setAttribute('aria-label','Abrir menú');
        btn.innerHTML='<i class="fa-solid fa-bars"></i>';
      }
      function toggle(){
        var open=!menu.classList.contains('aq-menu-open');
        menu.classList.toggle('aq-menu-open',open);
        btn.setAttribute('aria-expanded',String(open));
        btn.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');
        btn.innerHTML=open?'<i class="fa-solid fa-xmark"></i>':'<i class="fa-solid fa-bars"></i>';
      }
      btn.addEventListener('click',toggle);
      menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
      window.addEventListener('resize',function(){if(window.innerWidth>760) close();});
      document.addEventListener('keydown',function(e){if(e.key==='Escape') close();});
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',initNav); else initNav();
})();
