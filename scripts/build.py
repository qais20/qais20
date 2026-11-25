import html, os, glob
e = html.escape
SANS='-apple-system,BlinkMacSystemFont,&quot;Segoe UI&quot;,Helvetica,Arial,sans-serif'
MONO='ui-monospace,SFMono-Regular,Menlo,Consolas,monospace'
T = {
 "dark":  dict(bg="#0d1117", card="#161b22", border="#30363d", fg="#e6edf3", muted="#8b949e", acc="#3fb950", chipbg="#23863633", chipfg="#3fb950"),
 "light": dict(bg="#ffffff", card="#f6f8fa", border="#d0d7de", fg="#1f2328", muted="#59636e", acc="#1a7f37", chipbg="#dafbe1", chipfg="#1a7f37"),
}
cards = [
 ("nats","Real-time market data","Fintech",["NATS JetStream → ClickHouse pipeline,","3× replicated, bootstrapped fully in code."],"0 manual steps","NATS · ClickHouse"),
 ("migration","Prod migration < 1 week","Fintech",["Hand-deployed trading service moved into","its own prod account, all in Terraform."],"7 services · ~100 resources","ECS · Spacelift"),
 ("observability","Observability audit","Fintech",["Audited the Datadog estate, then set the","SLOs, runbooks and on-call routing."],"−46% spend · ~$30k/yr","Datadog"),
 ("aws","AWS cost review","Fintech",["Audited a ~$196k/month AWS estate,","account by account, workload by workload."],"$71–90k/mo savings found","AWS · FinOps"),
 ("eks","Production EKS","Travel tech",["First call for Kubernetes incidents and","upgrades across every environment."],"GitOps · Vault · Kaniko","EKS · Helm"),
 ("rca","Database incident RCA","Fintech",["Postgres timeouts traced to gp2 burst","exhaustion + swap. Fixed: gp3 + resize."],"service restored","RDS · CloudWatch"),
 ("secrets","Zero static credentials","Fintech",["OIDC for every pipeline. Risk services","moved off Vault to Secrets Manager."],"10 keys · 12 services","OIDC · IAM"),
 ("agents","Agents in production","Side work",["LLM support agent, plus a bug-fix agent","that opens PRs for a human to approve."],"human-in-the-loop","Claude · Python"),
]
for f in glob.glob("assets/work/*.svg"): os.remove(f)
os.makedirs("assets/work", exist_ok=True)
for key,title,org,desc,chip,tags in cards:
  for m,t in T.items():
    cw = int(len(chip)*9.7)+30
    open(f"assets/work/{key}-{m}.svg","w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 200" width="600" height="200" role="img" aria-label="{e(title)}">
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
stats = [("131","PRs merged, first 11 weeks"),("−46%","observability spend"),("6× CNCF","Kubestronaut"),("4 yrs","production AWS")]
for m,t in T.items():
  tiles=""
  for i,(big,small) in enumerate(stats):
    x=8+i*296
    tiles+=f'''<rect x="{x}" y="8" width="288" height="154" rx="12" fill="{t['card']}" stroke="{t['border']}"/>
  <text x="{x+24}" y="80" font-family="{SANS}" font-size="50" font-weight="700" fill="{t['fg']}" letter-spacing="-0.5">{e(big)}</text>
  <text x="{x+24}" y="126" font-family="{SANS}" font-size="20" fill="{t['muted']}">{e(small)}</text>
  '''
  open(f"assets/highlights-{m}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 170" width="1200" height="170" role="img" aria-label="131 PRs merged in first 11 weeks; -46% observability spend; 6 CNCF certifications including Kubestronaut; 4 years running production AWS">\n  {tiles}\n</svg>')
# banner subtitle
for m in T:
  p=f"assets/banner-{m}.svg"; s=open(p).read()
  s=s.replace("Platform engineering · applied AI · Dubai","Platform engineering · AWS · Kubernetes · Dubai")
  s=s.replace("problem → system → prod → pager","embed → untangle → ship → own")
  open(p,"w").write(s)
def pic(src, alt, w):
  return f'<picture><source media="(prefers-color-scheme: dark)" srcset="{src}-dark.svg"><img src="{src}-light.svg" width="{w}" alt="{e(alt)}"></picture>'
grid = "<p>" + "".join(pic(f"assets/work/{c[0]}", c[1], "50%") for c in cards) + "</p>"
readme = f'''{pic("assets/banner","Qais Navaei: platform engineering, AWS, Kubernetes, Dubai","100%")}

I get dropped into messy production systems, work out what the team actually needs, and leave behind infrastructure they can trust. I've built platforms for trading, risk, support and data teams in regulated fintech.

{pic("assets/highlights","Highlights","100%")}

### Selected work

{grid}

### Stack

<img src="https://skillicons.dev/icons?i=aws,kubernetes,terraform,docker,githubactions,gitlab,prometheus,grafana,postgres,redis,linux,bash,python&perline=13" height="44" alt="AWS, Kubernetes, Terraform, Docker, GitHub Actions, GitLab, Prometheus, Grafana, PostgreSQL, Redis, Linux, Bash, Python">

<sub>Plus Datadog · NATS JetStream · ClickHouse · Spacelift · Helm · ArgoCD · Vault · ECS Fargate</sub>

&nbsp;

[LinkedIn](https://linkedin.com/in/qais-navaei) &nbsp;·&nbsp; [Email](mailto:qaisbaraki81@gmail.com)
'''
open("README.md","w").write(readme)
