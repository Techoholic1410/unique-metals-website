const ENQUIRY_EMAIL = 'askus@uniquedecorativemetals.com';
const btn = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
btn.addEventListener('click', () => btn.setAttribute('aria-expanded', menu.classList.toggle('open')));
menu.addEventListener('click', e => { if (e.target.tagName === 'A') { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } });
document.getElementById('yr').textContent = new Date().getFullYear();

const form = document.getElementById('enquiry-form');
if (form) {
  const want = new URLSearchParams(location.search).get('product');
  if (want) {
    const opt = [...form.product.options].find(o => o.text === want);
    if (opt) form.product.value = opt.value;
  }
  form.addEventListener('submit', e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    const err = form.querySelector('.form-err');
    err.hidden = !!(d.name.trim() && d.phone.trim());
    if (!err.hidden) return;
    const text = `Hello Unique Decorative Metals,\nName: ${d.name}\nPhone: ${d.phone}\nCity: ${d.city || '-'}\nProduct: ${d.product}\nRequirement: ${d.msg || '-'}`;
    location.href = `mailto:${ENQUIRY_EMAIL}?subject=${encodeURIComponent('Enquiry: ' + d.product)}&body=${encodeURIComponent(text)}`;
  });
}
