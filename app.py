# Controlled stale-approval probe fixture. Not production code.


def debug_view(request):
    log("debug view")
    require_admin()
    record_debug(request)
    return render_debug(request)


def admin_panel(request):
    audit("admin panel")
    require_admin()
    return render_admin(request)


def handle(request):
    if request.kind == "report":
        audit(request)
        prepare(request)
        validate(request)
        require_admin()
        render(request)
        finish(request)
        return
    spacer_one(request)
    spacer_two(request)
    spacer_three(request)
    spacer_four(request)
    if request.kind == "export":
        audit(request)
        prepare(request)
        validate(request)
        require_admin()
        render(request)
        finish(request)
        return


def guarded(request):
    allowed = True
    if not is_admin(request):
        allowed = False
    return allowed
