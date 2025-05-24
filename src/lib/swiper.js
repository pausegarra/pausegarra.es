import Swiper from 'swiper';
import {Autoplay} from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

new Swiper('.swiper', {
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
