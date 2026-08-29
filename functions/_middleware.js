// www → apex 301. Pages _redirects cannot host-match (domain-level redirects unsupported).
// Path and query are preserved. HTTP is forced to https on the apex.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (url.hostname === "www.tv-mita.jp") {
    url.hostname = "tv-mita.jp";
    url.protocol = "https:";
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
