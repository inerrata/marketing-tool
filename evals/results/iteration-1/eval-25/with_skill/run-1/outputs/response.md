# How DNS Resolution Works

DNS (Domain Name System) is the internet's "phone book" — it translates human-readable domain names (like `www.example.com`) into IP addresses (like `93.184.216.34`) that computers use to communicate.

## The Key Players

- **DNS Resolver** (Recursive Resolver): Your computer or ISP's server that does the legwork of finding the answer.
- **Root Name Servers**: The top of the DNS hierarchy. They know where to find TLD servers.
- **TLD Name Servers**: Handle top-level domains like `.com`, `.org`, `.net`.
- **Authoritative Name Server**: The final authority for a specific domain; holds the actual DNS records.

## Step-by-Step Resolution Process

1. **You type a URL.** Your browser checks its local cache. If it already has the IP, it uses it and stops here.

2. **OS cache check.** If the browser doesn't have it, the operating system checks its own DNS cache (and the `hosts` file).

3. **Query sent to the recursive resolver.** Your device sends a query to its configured DNS resolver (usually your ISP's resolver or a public one like `8.8.8.8`). The resolver also checks its cache first.

4. **Resolver queries a root name server.** If the resolver has no cached answer, it asks one of the 13 root name server clusters: "Where do I find `.com`?" The root server responds with the address of the `.com` TLD name server.

5. **Resolver queries the TLD name server.** The resolver asks the `.com` TLD server: "Where do I find `example.com`?" It responds with the address of the authoritative name server for `example.com`.

6. **Resolver queries the authoritative name server.** The resolver asks that server: "What is the IP address for `www.example.com`?" The authoritative server returns the actual DNS record (e.g., an A record with the IP address).

7. **Answer returned and cached.** The resolver sends the IP back to your computer. Both the resolver and your OS cache the result for a period of time defined by the record's **TTL** (Time To Live).

8. **Connection established.** Your browser now connects directly to the IP address.

## Common DNS Record Types

| Type | Purpose |
|------|---------|
| **A** | Maps a domain to an IPv4 address |
| **AAAA** | Maps a domain to an IPv6 address |
| **CNAME** | Alias from one name to another |
| **MX** | Mail server for the domain |
| **TXT** | Arbitrary text (used for SPF, DKIM, verification) |
| **NS** | Specifies the authoritative name servers for the domain |

## Key Concepts

- **Recursive vs. Iterative queries**: The resolver does recursive lookups on your behalf (asking each server in turn). The resolver itself uses iterative queries when talking to root/TLD/authoritative servers.
- **TTL (Time To Live)**: How long a DNS record is cached, in seconds. Low TTL = faster propagation of changes; high TTL = less DNS traffic.
- **DNS caching**: Occurs at multiple layers (browser, OS, resolver) to reduce latency and load.
- **DNSSEC**: An extension that adds cryptographic signatures to DNS records to prevent spoofing/poisoning attacks.

## Why This Matters

The entire process — from your browser to root server to authoritative server and back — typically takes **20–120 milliseconds**, and most of it is hidden by caching. Without DNS, you'd have to memorize IP addresses for every website you visit.
