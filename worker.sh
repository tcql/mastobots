

function subst() { eval echo -E "$2"; }

# Force evaluation of env vars embedded in config template
cat config.cfg.tmpl | mapfile -c 1 -C subst > config.cfg

ananas config.cfg
