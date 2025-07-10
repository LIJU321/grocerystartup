import secrets

class CSPNonceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ✅ generate a secure nonce
        request.csp_nonce = secrets.token_urlsafe(16)

        response = self.get_response(request)

        # ✅ inject nonce into the CSP header
        nonce = request.csp_nonce
        response["Content-Security-Policy"] = (
            f"default-src 'self'; "
            f"script-src 'self' 'nonce-{nonce}'; "
            f"style-src 'self' 'nonce-{nonce}'; "
            f"img-src 'self'; "
            f"connect-src 'self'; "
            f"font-src 'self'; "
            f"object-src 'none'; "
            f"media-src 'self'; "
            f"frame-src 'none'; "
            f"frame-ancestors 'none'; "
            f"form-action 'self'; "
            f"base-uri 'self';"
        )

        return response
