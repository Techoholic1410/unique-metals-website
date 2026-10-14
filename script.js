const WA_NUMBER = '910000000000'; // TODO: replace with the real WhatsApp number (country code + number, no +)
const btn = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
btn.addEventListener('click', () => btn.setAttribute('aria-expanded', menu.classList.toggle('open')));
menu.addEventListener('click', e => { if (e.target.tagName === 'A') { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } });
document.getElementById('yr').textContent = new Date().getFullYear();

const form = document.getElementById('enquiry-form');
document.querySelectorAll('[data-product]').forEach(a => a.addEventListener('click', () => {
  const opt = [...form.product.options].find(o => o.text === a.dataset.product);
  if (opt) form.product.value = opt.value || opt.text;
}));
form.addEventListener('submit', e => {
  e.preventDefault();
  const d = Object.fromEntries(new FormData(form));
  const err = form.querySelector('.form-err');
  err.hidden = !!(d.name.trim() && d.phone.trim());
  if (!err.hidden) return;
  const text = `Hello Unique Decorative Metals,\nName: ${d.name}\nPhone: ${d.phone}\nCity: ${d.city || '-'}\nProduct: ${d.product}\nRequirement: ${d.msg || '-'}`;
  window.open(`https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
});
