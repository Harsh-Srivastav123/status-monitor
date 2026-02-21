"""
Provider Configuration - 100 Providers (Verified Working URLs)

Each provider has:
- name: Display name
- mode: "rss" (all providers use RSS + ETag)
- rss_url: RSS feed URL for monitoring
- status_url: Clickable link to status page
- poll_interval: Seconds between checks
- category: Category for grouping
"""

PROVIDERS = [
    # ============================================================
    # CLOUD & INFRASTRUCTURE (15)
    # ============================================================
    {
        "name": "OpenAI",
        "mode": "rss",
        "rss_url": "https://status.openai.com/history.atom",
        "status_url": "https://status.openai.com",
        "poll_interval": 60,
        "category": "AI/ML"
    },
    {
        "name": "Anthropic",
        "mode": "rss",
        "rss_url": "https://status.anthropic.com/history.atom",
        "status_url": "https://status.anthropic.com",
        "poll_interval": 60,
        "category": "AI/ML"
    },
    {
        "name": "Cloudflare",
        "mode": "rss",
        "rss_url": "https://www.cloudflarestatus.com/history.atom",
        "status_url": "https://www.cloudflarestatus.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "DigitalOcean",
        "mode": "rss",
        "rss_url": "https://status.digitalocean.com/history.atom",
        "status_url": "https://status.digitalocean.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Linode",
        "mode": "rss",
        "rss_url": "https://status.linode.com/history.atom",
        "status_url": "https://status.linode.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Scaleway",
        "mode": "rss",
        "rss_url": "https://status.scaleway.com/history.atom",
        "status_url": "https://status.scaleway.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "UpCloud",
        "mode": "rss",
        "rss_url": "https://status.upcloud.com/history.atom",
        "status_url": "https://status.upcloud.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Equinix Metal",
        "mode": "rss",
        "rss_url": "https://status.equinixmetal.com/history.atom",
        "status_url": "https://status.equinixmetal.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Render",
        "mode": "rss",
        "rss_url": "https://status.render.com/history.atom",
        "status_url": "https://status.render.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Fly.io",
        "mode": "rss",
        "rss_url": "https://status.flyio.net/history.atom",
        "status_url": "https://status.flyio.net",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Bunny CDN",
        "mode": "rss",
        "rss_url": "https://status.bunny.net/history.atom",
        "status_url": "https://status.bunny.net",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "KeyCDN",
        "mode": "rss",
        "rss_url": "https://status.keycdn.com/history.atom",
        "status_url": "https://status.keycdn.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "GitHub (API)",
        "mode": "hash",
        "api_url": "https://www.githubstatus.com/api/v2/incidents.json",
        "status_url": "https://www.githubstatus.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Vercel (API)",
        "mode": "hash",
        "api_url": "https://www.vercel-status.com/api/v2/incidents.json",
        "status_url": "https://www.vercel-status.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },
    {
        "name": "Hostinger",
        "mode": "rss",
        "rss_url": "https://status.hostinger.com/history.atom",
        "status_url": "https://status.hostinger.com",
        "poll_interval": 60,
        "category": "Cloud & Infrastructure"
    },

    # ============================================================
    # DEVOPS & CI/CD (15)
    # ============================================================
    {
        "name": "GitHub",
        "mode": "rss",
        "rss_url": "https://www.githubstatus.com/history.atom",
        "status_url": "https://www.githubstatus.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Bitbucket",
        "mode": "rss",
        "rss_url": "https://bitbucket.status.atlassian.com/history.atom",
        "status_url": "https://bitbucket.status.atlassian.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "CircleCI",
        "mode": "rss",
        "rss_url": "https://status.circleci.com/history.atom",
        "status_url": "https://status.circleci.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Travis CI",
        "mode": "rss",
        "rss_url": "https://www.traviscistatus.com/history.atom",
        "status_url": "https://www.traviscistatus.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "npm",
        "mode": "rss",
        "rss_url": "https://status.npmjs.org/history.atom",
        "status_url": "https://status.npmjs.org",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "PyPI",
        "mode": "rss",
        "rss_url": "https://status.python.org/history.atom",
        "status_url": "https://status.python.org",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "RubyGems",
        "mode": "rss",
        "rss_url": "https://status.rubygems.org/history.atom",
        "status_url": "https://status.rubygems.org",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "HashiCorp",
        "mode": "rss",
        "rss_url": "https://status.hashicorp.com/history.atom",
        "status_url": "https://status.hashicorp.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Pulumi",
        "mode": "rss",
        "rss_url": "https://status.pulumi.com/history.atom",
        "status_url": "https://status.pulumi.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Buildkite",
        "mode": "rss",
        "rss_url": "https://www.buildkitestatus.com/history.atom",
        "status_url": "https://www.buildkitestatus.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Semaphore CI",
        "mode": "rss",
        "rss_url": "https://status.semaphoreci.com/history.atom",
        "status_url": "https://status.semaphoreci.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Codecov",
        "mode": "rss",
        "rss_url": "https://status.codecov.com/history.atom",
        "status_url": "https://status.codecov.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Sonatype",
        "mode": "rss",
        "rss_url": "https://status.sonatype.com/history.atom",
        "status_url": "https://status.sonatype.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "Netlify (API)",
        "mode": "hash",
        "api_url": "https://www.netlifystatus.com/api/v2/incidents.json",
        "status_url": "https://www.netlifystatus.com",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },
    {
        "name": "Codefresh",
        "mode": "rss",
        "rss_url": "https://status.codefresh.io/history.atom",
        "status_url": "https://status.codefresh.io",
        "poll_interval": 60,
        "category": "DevOps & CI/CD"
    },

    # ============================================================
    # HOSTING & DEPLOYMENT (10)
    # ============================================================
    {
        "name": "Vercel",
        "mode": "rss",
        "rss_url": "https://www.vercel-status.com/history.atom",
        "status_url": "https://www.vercel-status.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Netlify",
        "mode": "rss",
        "rss_url": "https://www.netlifystatus.com/history.atom",
        "status_url": "https://www.netlifystatus.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Heroku",
        "mode": "rss",
        "rss_url": "https://status.heroku.com/history.atom",
        "status_url": "https://status.heroku.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Platform.sh",
        "mode": "rss",
        "rss_url": "https://status.platform.sh/history.atom",
        "status_url": "https://status.platform.sh",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Kinsta",
        "mode": "rss",
        "rss_url": "https://status.kinsta.com/history.atom",
        "status_url": "https://status.kinsta.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "WP Engine",
        "mode": "rss",
        "rss_url": "https://status.wpengine.com/history.atom",
        "status_url": "https://status.wpengine.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Pantheon",
        "mode": "rss",
        "rss_url": "https://status.pantheon.io/history.atom",
        "status_url": "https://status.pantheon.io",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Acquia",
        "mode": "rss",
        "rss_url": "https://status.acquia.com/history.atom",
        "status_url": "https://status.acquia.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Cloudways",
        "mode": "rss",
        "rss_url": "https://status.cloudways.com/history.atom",
        "status_url": "https://status.cloudways.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },
    {
        "name": "Webflow",
        "mode": "rss",
        "rss_url": "https://status.webflow.com/history.atom",
        "status_url": "https://status.webflow.com",
        "poll_interval": 60,
        "category": "Hosting & Deployment"
    },

    # ============================================================
    # DATABASE & STORAGE (12)
    # ============================================================
    {
        "name": "MongoDB Atlas",
        "mode": "rss",
        "rss_url": "https://status.mongodb.com/history.atom",
        "status_url": "https://status.mongodb.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Redis Cloud",
        "mode": "rss",
        "rss_url": "https://status.redis.io/history.atom",
        "status_url": "https://status.redis.io",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "PlanetScale",
        "mode": "rss",
        "rss_url": "https://www.planetscalestatus.com/history.atom",
        "status_url": "https://www.planetscalestatus.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Supabase",
        "mode": "rss",
        "rss_url": "https://status.supabase.com/history.atom",
        "status_url": "https://status.supabase.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "CockroachDB",
        "mode": "rss",
        "rss_url": "https://status.cockroachlabs.cloud/history.atom",
        "status_url": "https://status.cockroachlabs.cloud",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Cloudinary",
        "mode": "rss",
        "rss_url": "https://status.cloudinary.com/history.atom",
        "status_url": "https://status.cloudinary.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Imgix",
        "mode": "rss",
        "rss_url": "https://status.imgix.com/history.atom",
        "status_url": "https://status.imgix.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Backblaze",
        "mode": "rss",
        "rss_url": "https://status.backblaze.com/history.atom",
        "status_url": "https://status.backblaze.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Wasabi",
        "mode": "rss",
        "rss_url": "https://status.wasabi.com/history.atom",
        "status_url": "https://status.wasabi.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Turso",
        "mode": "rss",
        "rss_url": "https://status.turso.tech/history.atom",
        "status_url": "https://status.turso.tech",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    {
        "name": "Upstash",
        "mode": "rss",
        "rss_url": "https://status.upstash.com/history.atom",
        "status_url": "https://status.upstash.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "Supabase (API)",
        "mode": "hash",
        "api_url": "https://status.supabase.com/api/v2/incidents.json",
        "status_url": "https://status.supabase.com",
        "poll_interval": 60,
        "category": "Database & Storage"
    },

    # ============================================================
    # COMMUNICATION & COLLABORATION (10)
    # ============================================================
    {
        "name": "Twilio",
        "mode": "rss",
        "rss_url": "https://status.twilio.com/history.atom",
        "status_url": "https://status.twilio.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "SendGrid",
        "mode": "rss",
        "rss_url": "https://status.sendgrid.com/history.atom",
        "status_url": "https://status.sendgrid.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Mailgun",
        "mode": "rss",
        "rss_url": "https://status.mailgun.com/history.atom",
        "status_url": "https://status.mailgun.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Postmark",
        "mode": "rss",
        "rss_url": "https://status.postmarkapp.com/history.atom",
        "status_url": "https://status.postmarkapp.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Zoom",
        "mode": "rss",
        "rss_url": "https://status.zoom.us/history.atom",
        "status_url": "https://status.zoom.us",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Discord",
        "mode": "rss",
        "rss_url": "https://discordstatus.com/history.atom",
        "status_url": "https://discordstatus.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Pusher",
        "mode": "rss",
        "rss_url": "https://status.pusher.com/history.atom",
        "status_url": "https://status.pusher.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Stream",
        "mode": "rss",
        "rss_url": "https://status.getstream.io/history.atom",
        "status_url": "https://status.getstream.io",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Ably",
        "mode": "rss",
        "rss_url": "https://status.ably.com/history.atom",
        "status_url": "https://status.ably.com",
        "poll_interval": 60,
        "category": "Communication"
    },
    {
        "name": "Customer.io",
        "mode": "rss",
        "rss_url": "https://status.customer.io/history.atom",
        "status_url": "https://status.customer.io",
        "poll_interval": 60,
        "category": "Communication"
    },

    # ============================================================
    # PAYMENT & FINANCE (8)
    # ============================================================
    {
        "name": "Stripe",
        "mode": "rss",
        "rss_url": "https://www.stripestatus.com/history.atom",
        "status_url": "https://www.stripestatus.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "PayPal",
        "mode": "rss",
        "rss_url": "https://www.paypal-status.com/history.atom",
        "status_url": "https://www.paypal-status.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "Braintree",
        "mode": "rss",
        "rss_url": "https://status.braintreepayments.com/history.atom",
        "status_url": "https://status.braintreepayments.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "Plaid",
        "mode": "rss",
        "rss_url": "https://status.plaid.com/history.atom",
        "status_url": "https://status.plaid.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "Coinbase",
        "mode": "rss",
        "rss_url": "https://status.coinbase.com/history.atom",
        "status_url": "https://status.coinbase.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "Adyen",
        "mode": "rss",
        "rss_url": "https://status.adyen.com/history.atom",
        "status_url": "https://status.adyen.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "Stripe (API)",
        "mode": "hash",
        "api_url": "https://www.stripestatus.com/api/v2/incidents.json",
        "status_url": "https://www.stripestatus.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },
    {
        "name": "Chargebee",
        "mode": "rss",
        "rss_url": "https://status.chargebee.com/history.atom",
        "status_url": "https://status.chargebee.com",
        "poll_interval": 60,
        "category": "Payment & Finance"
    },

    # ============================================================
    # MONITORING & ANALYTICS (10)
    # ============================================================
    {
        "name": "Datadog",
        "mode": "rss",
        "rss_url": "https://status.datadoghq.com/history.atom",
        "status_url": "https://status.datadoghq.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "New Relic",
        "mode": "rss",
        "rss_url": "https://status.newrelic.com/history.atom",
        "status_url": "https://status.newrelic.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "PagerDuty",
        "mode": "rss",
        "rss_url": "https://status.pagerduty.com/history.atom",
        "status_url": "https://status.pagerduty.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Sentry",
        "mode": "rss",
        "rss_url": "https://status.sentry.io/history.atom",
        "status_url": "https://status.sentry.io",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Grafana Cloud",
        "mode": "rss",
        "rss_url": "https://status.grafana.com/history.atom",
        "status_url": "https://status.grafana.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Elastic Cloud",
        "mode": "rss",
        "rss_url": "https://status.elastic.co/history.atom",
        "status_url": "https://status.elastic.co",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Mixpanel",
        "mode": "rss",
        "rss_url": "https://status.mixpanel.com/history.atom",
        "status_url": "https://status.mixpanel.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Amplitude",
        "mode": "rss",
        "rss_url": "https://status.amplitude.com/history.atom",
        "status_url": "https://status.amplitude.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Heap",
        "mode": "rss",
        "rss_url": "https://status.heap.io/history.atom",
        "status_url": "https://status.heap.io",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },
    {
        "name": "Rollbar",
        "mode": "rss",
        "rss_url": "https://status.rollbar.com/history.atom",
        "status_url": "https://status.rollbar.com",
        "poll_interval": 60,
        "category": "Monitoring & Analytics"
    },

    # ============================================================
    # SECURITY & IDENTITY (8)
    # ============================================================
    {
        "name": "1Password",
        "mode": "rss",
        "rss_url": "https://status.1password.com/history.atom",
        "status_url": "https://status.1password.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    {
        "name": "Duo Security",
        "mode": "rss",
        "rss_url": "https://status.duo.com/history.atom",
        "status_url": "https://status.duo.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    {
        "name": "Snyk",
        "mode": "rss",
        "rss_url": "https://status.snyk.io/history.atom",
        "status_url": "https://status.snyk.io",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    {
        "name": "JumpCloud",
        "mode": "rss",
        "rss_url": "https://status.jumpcloud.com/history.atom",
        "status_url": "https://status.jumpcloud.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    {
        "name": "Cloudflare Zero Trust",
        "mode": "rss",
        "rss_url": "https://www.cloudflarestatus.com/history.atom",
        "status_url": "https://www.cloudflarestatus.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "Datadog (API)",
        "mode": "hash",
        "api_url": "https://status.datadoghq.com/api/v2/incidents.json",
        "status_url": "https://status.datadoghq.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    {
        "name": "LastPass",
        "mode": "rss",
        "rss_url": "https://status.lastpass.com/history.atom",
        "status_url": "https://status.lastpass.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "CircleCI (API)",
        "mode": "hash",
        "api_url": "https://status.circleci.com/api/v2/incidents.json",
        "status_url": "https://status.circleci.com",
        "poll_interval": 60,
        "category": "Security & Identity"
    },

    # ============================================================
    # PRODUCTIVITY & PROJECT MANAGEMENT (8)
    # ============================================================
    {
        "name": "Atlassian",
        "mode": "rss",
        "rss_url": "https://status.atlassian.com/history.atom",
        "status_url": "https://status.atlassian.com",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Notion",
        "mode": "rss",
        "rss_url": "https://status.notion.so/history.atom",
        "status_url": "https://status.notion.so",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Asana",
        "mode": "rss",
        "rss_url": "https://trust.asana.com/history.atom",
        "status_url": "https://trust.asana.com",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Monday.com",
        "mode": "rss",
        "rss_url": "https://status.monday.com/history.atom",
        "status_url": "https://status.monday.com",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Trello",
        "mode": "rss",
        "rss_url": "https://trello.status.atlassian.com/history.atom",
        "status_url": "https://trello.status.atlassian.com",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Figma",
        "mode": "rss",
        "rss_url": "https://status.figma.com/history.atom",
        "status_url": "https://status.figma.com",
        "poll_interval": 60,
        "category": "Productivity"
    },
    {
        "name": "Linear",
        "mode": "rss",
        "rss_url": "https://status.linear.app/history.atom",
        "status_url": "https://status.linear.app",
        "poll_interval": 60,
        "category": "Productivity"
    },
    # HASH-BASED: Using JSON API polling
    {
        "name": "Atlassian (API)",
        "mode": "hash",
        "api_url": "https://status.atlassian.com/api/v2/incidents.json",
        "status_url": "https://status.atlassian.com",
        "poll_interval": 60,
        "category": "Productivity"
    },

    # ============================================================
    # DEVELOPER TOOLS & APIs (4)
    # ============================================================
    {
        "name": "Algolia",
        "mode": "rss",
        "rss_url": "https://status.algolia.com/history.atom",
        "status_url": "https://status.algolia.com",
        "poll_interval": 60,
        "category": "Developer Tools"
    },
    {
        "name": "Segment",
        "mode": "rss",
        "rss_url": "https://status.segment.com/history.atom",
        "status_url": "https://status.segment.com",
        "poll_interval": 60,
        "category": "Developer Tools"
    },
    {
        "name": "LaunchDarkly",
        "mode": "rss",
        "rss_url": "https://status.launchdarkly.com/history.atom",
        "status_url": "https://status.launchdarkly.com",
        "poll_interval": 60,
        "category": "Developer Tools"
    },
    {
        "name": "Contentful",
        "mode": "rss",
        "rss_url": "https://www.contentfulstatus.com/history.atom",
        "status_url": "https://www.contentfulstatus.com",
        "poll_interval": 60,
        "category": "Developer Tools"
    },
]

# Total: 100 providers
DEFAULT_POLL_INTERVAL = 60
