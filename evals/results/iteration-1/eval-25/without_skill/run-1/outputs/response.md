# How DNS Resolution Works

DNS (Domain Name System) is often called the "phone book of the internet." It translates human-readable domain names (like `www.example.com`) into IP addresses (like `93.184.216.34`) that computers use to communicate.

## The Basic Idea

When you type a URL into your browser, your computer doesn't inherently know where that server lives. It needs an IP address. DNS resolution is the process of looking up that address.

---

## Step-by-Step DNS Resolution

### 1. Browser Cache Check
Your browser first checks its own local cache. If you recently visited the site, it may already know the IP address and skip the rest of the process entirely.

### 2. Operating System Cache
If the browser doesn't have it, it asks the operating system. The OS checks its own DNS cache and also the `hosts` file (a local file that can map hostnames to IPs manually).

### 3. Recursive Resolver (Your ISP or Configured DNS Server)
If the OS doesn't have the answer, the query goes to a **recursive resolver** — typically provided by your ISP, or a public one like Google (`8.8.8.8`) or Cloudflare (`1.1.1.1`).

The recursive resolver does the heavy lifting. It either answers from its own cache or starts hunting for the answer on your behalf.

### 4. Root Name Servers
If the resolver doesn't have the answer cached, it contacts one of the **13 root name server clusters** (e.g., `a.root-servers.net`). These servers don't know the IP for `www.example.com`, but they know who's responsible for `.com` domains.

The root server responds: "Go ask the `.com` TLD name server."

### 5. TLD Name Servers
The resolver now contacts the **Top-Level Domain (TLD) name server** for `.com`. This server doesn't know the exact IP either, but it knows which **authoritative name servers** are responsible for `example.com`.

The TLD server responds: "Go ask `ns1.example.com`."

### 6. Authoritative Name Server
The resolver contacts the **authoritative name server** for `example.com`. This server has the definitive DNS records for that domain and responds with the actual IP address: `93.184.216.34`.

### 7. Response Returned to Client
The recursive resolver returns the IP address to your OS, which passes it to your browser. The resolver also caches this result for future queries (for a duration specified by the record's **TTL — Time to Live**).

### 8. Connection Established
Your browser now has the IP address and can establish a TCP connection to the web server at that address to load the website.

---

## Key DNS Record Types

| Record | Purpose |
|--------|---------|
| **A** | Maps a domain to an IPv4 address |
| **AAAA** | Maps a domain to an IPv6 address |
| **CNAME** | Alias that points one domain to another domain |
| **MX** | Specifies mail servers for the domain |
| **NS** | Lists the authoritative name servers for the domain |
| **TXT** | Stores arbitrary text (used for verification, SPF, DKIM, etc.) |
| **PTR** | Reverse lookup — maps an IP address back to a domain name |

---

## TTL and Caching

Every DNS record has a **TTL (Time to Live)** value measured in seconds. This tells resolvers how long to cache the record before checking for a fresh answer. Common TTL values range from 300 seconds (5 minutes) to 86400 seconds (24 hours).

- **Short TTL**: Changes propagate faster, but more DNS queries are made.
- **Long TTL**: Faster performance (more cache hits), but changes take longer to propagate globally.

---

## The Full Journey Visualized

```
Your Browser
    |
    v
OS DNS Cache / hosts file
    |
    v
Recursive Resolver (ISP / 8.8.8.8 / 1.1.1.1)
    |
    v
Root Name Server  -->  "Ask the .com TLD server"
    |
    v
.com TLD Name Server  -->  "Ask ns1.example.com"
    |
    v
Authoritative Name Server (ns1.example.com)
    |
    v
IP Address returned: 93.184.216.34
    |
    v
Your Browser connects to 93.184.216.34
```

---

## Summary

DNS resolution is a hierarchical, distributed lookup system. Most queries are answered quickly from cache. When a full lookup is needed, the recursive resolver walks down the DNS hierarchy — from root servers to TLD servers to authoritative servers — to find the definitive answer. The result is cached at multiple layers to make future lookups faster.
