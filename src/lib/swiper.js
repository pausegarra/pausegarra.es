import Swiper from 'swiper';
import { Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

let swiperInstance;

function initSwiper() {
  if (swiperInstance) {
    swiperInstance.destroy(true, true);
  }

  const el = document.querySelector('.swiper');
  if (!el) return;

  swiperInstance = new Swiper(el, {
    loop: true,
    modules: [Autoplay],
    spaceBetween: 20,
    slidesPerView: 2,
    breakpoints: {
      640: { slidesPerView: 3 },
      768: { slidesPerView: 4 },
      1024: { slidesPerView: 8 },
    },
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
  });
}

document.addEventListener('DOMContentLoaded', initSwiper);

document.addEventListener('astro:after-swap', initSwiper);