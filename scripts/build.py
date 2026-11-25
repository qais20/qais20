import html, os, glob
e = html.escape
SANS='-apple-system,BlinkMacSystemFont,&quot;Segoe UI&quot;,Helvetica,Arial,sans-serif'
MONO='ui-monospace,SFMono-Regular,Menlo,Consolas,monospace'
T = {
 "dark":  dict(bg="#0d1117", card="#161b22", border="#30363d", fg="#e6edf3", muted="#8b949e", acc="#3fb950", chipbg="#23863633", chipfg="#3fb950"),
 "light": dict(bg="#ffffff", card="#f6f8fa", border="#d0d7de", fg="#1f2328", muted="#59636e", acc="#1a7f37", chipbg="#dafbe1", chipfg="#1a7f37"),
}
cards = [
 ("pricing","Pricing engine to prod","Fintech",["The quant team's hand-run FIX → NATS →","ClickHouse engine, turned into a real prod stack."],"< 1 week · 7 services","NATS · ClickHouse"),
 ("support","Support stack, end to end","Fintech",["Helpdesk off a hand-managed box onto ECS;","SLA dashboard shipped past security review."],"1 box → ECS + CI/CD","NestJS · SES"),
 ("copytrading","Copy-trading launch","Fintech",["Stood up a new product's whole stack: MT5","+ cTrader bridges, NATS, Django, e2e envs."],"on-demand test envs","NATS · Django"),
 ("agent","Slack bug → prod fix","Side work",["Report a bug in Slack: a sandboxed agent","opens the PR, a human approves, it ships."],"kill switch · human approves","Claude · Python"),
 ("mcp","MCP for a closed app","Side work",["No public API? Built an MCP server that","drives the site so Claude can act on it."],"remote connector · auth","MCP · Playwright"),
 ("outage","Killed a recurring outage","Fintech",["Internal tools kept timing out. Traced it to","Postgres burst exhaustion, fixed it, alerted on it."],"root cause, not restart","RDS · CloudWatch"),
 ("service","Infra as a service","Fintech",["One front door, on-call rota, 10-min SLA on","critical. Promise: infra in < 1 business day."],"47 tickets · 4 incidents","SRE"),
 ("datadog","Datadog bill −46%","Fintech",["Switched off what nobody used, then rebuilt","alerting: SLOs, runbooks, on-call routing."],"~$30k/yr saved","Datadog · Terraform"),
 ("k8s","Prod Kubernetes","Travel tech",["First call for EKS incidents and upgrades.","Killed privileged builds and static secrets."],"Kaniko · Vault · GitOps","EKS · Helm"),
 ("modules","Paved road, in code","Fintech",["Reusable Terraform modules, so every new","service ships with monitoring and DB alerts."],"observability by default","Terraform"),
]
for f in glob.glob("assets/cases/*.svg"): os.remove(f)
os.makedirs("assets/cases", exist_ok=True)
for key,title,org,desc,chip,tags in cards:
  for m,t in T.items():
    cw = int(len(chip)*9.7)+30
    open(f"assets/cases/{key}-{m}.svg","w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="600" height="200" role="img" aria-label="{e(title)}">
  <rect x="8" y="8" width="584" height="184" rx="12" fill="{t['card']}" stroke="{t['border']}"/>
  <circle cx="44" cy="50" r="6" fill="{t['acc']}"/>
  <text x="60" y="59" font-family="{SANS}" font-size="27" font-weight="600" fill="{t['fg']}">{e(title)}</text>
  <text x="562" y="57" text-anchor="end" font-family="{MONO}" font-size="14" fill="{t['muted']}">{e(org)}</text>
  <text x="38" y="98" font-family="{SANS}" font-size="20" fill="{t['muted']}">{e(desc[0])}</text>
  <text x="38" y="124" font-family="{SANS}" font-size="20" fill="{t['muted']}">{e(desc[1])}</text>
  <rect x="38" y="144" width="{cw}" height="32" rx="16" fill="{t['chipbg']}"/>
  <text x="53" y="165" font-family="{MONO}" font-size="16" font-weight="600" fill="{t['chipfg']}">{e(chip)}</text>
  <text x="562" y="165" text-anchor="end" font-family="{MONO}" font-size="15" fill="{t['muted']}">{e(tags)}</text>
</svg>''')
# stats strip
stats = [("131","PRs merged, first 11 weeks"),("4 teams","taken to production"),("6× CNCF","Kubestronaut")]
for m,t in T.items():
  tiles=""
  for i,(big,small) in enumerate(stats):
    x=8+i*400
    tiles+=f'''<rect x="{x}" y="8" width="384" height="154" rx="12" fill="{t['card']}" stroke="{t['border']}"/>
  <text x="{x+24}" y="80" font-family="{SANS}" font-size="50" font-weight="700" fill="{t['fg']}" letter-spacing="-0.5">{e(big)}</text>
  <text x="{x+24}" y="126" font-family="{SANS}" font-size="20" fill="{t['muted']}">{e(small)}</text>
  '''
  open(f"assets/numbers-{m}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 170" width="1200" height="170" role="img" aria-label="131 PRs merged in first 11 weeks; 4 teams taken to production; 6 CNCF certifications including Kubestronaut">\n  {tiles}\n</svg>')
steps=[("01","Embed","Sit with the team that","has the problem."),("02","Untangle","Find the real problem","behind the ticket."),("03","Ship","Smallest fix that works,","live in production."),("04","Own","Alerts, runbooks, on-call.","Then hand it over.")]
for m,t in T.items():
  g=""
  for i,(n,h,a,b) in enumerate(steps):
    x=8+i*298
    g+=f'''<rect x="{x}" y="8" width="290" height="164" rx="12" fill="{t['card']}" stroke="{t['border']}"/>
  <text x="{x+24}" y="48" font-family="{MONO}" font-size="16" fill="{t['acc']}">{n}</text>
  <text x="{x+24}" y="90" font-family="{SANS}" font-size="30" font-weight="700" fill="{t['fg']}">{h}</text>
  <text x="{x+24}" y="124" font-family="{SANS}" font-size="18" fill="{t['muted']}">{e(a)}</text>
  <text x="{x+24}" y="148" font-family="{SANS}" font-size="18" fill="{t['muted']}">{e(b)}</text>
  '''
    if i<3: g+=f'<text x="{x+282}" y="96" text-anchor="middle" font-family="{SANS}" font-size="20" fill="{t["acc"]}" opacity="0">→</text>\n  '
  open(f"assets/method-{m}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 180" width="1200" height="180" role="img" aria-label="How I work: embed with the team, untangle the real problem, ship the smallest fix to production, own it with alerts and runbooks then hand over.">\n  {g}\n</svg>')
# banner: hand-made, assets/hero-*.svg
def pic(src, alt, w):
  return f'<picture><source media="(prefers-color-scheme: dark)" srcset="{src}-dark.svg"><img src="{src}-light.svg" width="{w}" alt="{e(alt)}"></picture>'
grid = "<p>" + "".join(pic(f"assets/cases/{c[0]}", c[1], "50%") for c in cards) + "</p>"
readme = f'''{pic("assets/cover","Qais Navaei: platform engineering, AWS, Kubernetes, Dubai","100%")}

I get dropped into messy production systems, work out what the team actually needs, and leave behind infrastructure they can trust. I've built platforms for trading, risk, support and data teams in regulated fintech.

{pic("assets/numbers","Highlights","100%")}

### How I work

{pic("assets/method","How I work","100%")}

### Selected work

{grid}

### Stack

<img src="https://skillicons.dev/icons?i=aws,kubernetes,terraform,docker,githubactions,gitlab,prometheus,grafana,postgres,redis,linux,bash,python&perline=13" height="44" alt="AWS, Kubernetes, Terraform, Docker, GitHub Actions, GitLab, Prometheus, Grafana, PostgreSQL, Redis, Linux, Bash, Python">

<sub>Plus Datadog · NATS JetStream · ClickHouse · Spacelift · Helm · ArgoCD · Vault · MCP · Claude Code</sub>

&nbsp;

Got a messy system and a team waiting on it? Let's talk.

[LinkedIn](https://linkedin.com/in/qais-navaei) &nbsp;·&nbsp; [Email](mailto:qaisbaraki81@gmail.com)
'''
open("README.md","w").write(readme)
