// オフラインでも遊べるように、アプリ本体と地図・ライブラリをキャッシュする。
// アプリを更新したら VERSION を上げる（tools/build.py が自動で書き換える）。
const VERSION = "20261006140141";
const CACHE = "atlas197-" + VERSION;
const PRECACHE = [
  "./", "./index.html", "./world.json", "./manifest.webmanifest",
  "./icons/icon-192.png", "./icons/icon-512.png", "./icons/apple-touch-icon.png",
  "https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js",
  "https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"
];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith("atlas197-") && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

// キャッシュがあればすぐ返し、裏で新しい版を取りに行く（フォントも同じ扱い）
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.open(CACHE).then(async cache => {
    const hit = await cache.match(e.request, { ignoreSearch: e.request.mode === "navigate" });
    const net = fetch(e.request).then(res => {
      if (res && (res.ok || res.type === "opaque")) cache.put(e.request, res.clone());
      return res;
    }).catch(() => hit);
    return hit || net;
  }));
});
