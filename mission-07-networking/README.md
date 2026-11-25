# Mission 7 — How computers communicate

## 1. Task / objective
Explain the basic types of networks and key network ideas, observe connectivity and DNS information from the Terminal,
and describe step by step what happens when a website opens.

## 2. Work completed
- Completed the network concepts table with my own words and an example for each (Task 7.1).
- Ran `ping` and `nslookup` against the public example domain `example.com` (Task 7.2).
- Wrote a 7-step explanation of opening a website (Task 7.3).
- Saved the output in [`../evidence/mission-07-network-output.txt`](../evidence/mission-07-network-output.txt), with my
  own DNS server / router address removed.

### Task 7.1 — Network concepts

| Concept | Explained in my own words | Example |
|---------|---------------------------|---------|
| LAN | A network covering a small area, such as a home, lab or office. Devices are close together and usually owned by one person or organisation. | My home Wi-Fi connecting my laptop, phone and smart TV. |
| MAN | A network covering a city or large campus area, linking several LANs. | A university network joining hostels, library and departments across one campus, or a city's cable network. |
| WAN | A network covering large geographical areas — countries or the whole world — by joining many smaller networks. | The Internet; a bank linking its branches across India. |
| DNS | The "phone book" of the Internet: it translates a domain name that humans remember into the IP address that computers use. | `example.com` → `172.66.147.243` |
| Router | A device that connects different networks and forwards data packets towards the right destination. | The Wi-Fi router at home connecting my LAN to my internet provider. |
| Protocol | A set of rules that devices follow so they understand each other — like a common language and etiquette. | HTTP/HTTPS for web pages, TCP/IP for delivering data, DNS for name lookups. |
| Packet switching | Data is broken into small packets; each travels across the network (maybe by different routes) and they are put back together at the destination. | A photo I upload is split into many packets and rebuilt by the server. |
| Client-server | A client asks for a service and a server provides it. | My browser (client) requests a page from GitHub's web server (server). |

### Task 7.2 — Observe network information

**Connectivity test — `ping -c 4 example.com`**
```
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.272/5.764/8.561/1.696 ms
```

**DNS lookup — `nslookup example.com`** (my own DNS server lines removed)
```
Non-authoritative answer:
Name:    example.com
Address: 104.20.23.154
Name:    example.com
Address: 172.66.147.243
```

- **What a connectivity test checks:** `ping` sends small test packets to a host and waits for replies. It tells me
  whether my computer can reach that host at all, how long a round trip takes (here about 6 ms on average) and whether
  any packets were lost (here 0%).
- **What a DNS lookup displays:** the IP address (or addresses) linked to a domain name. `example.com` has two addresses,
  which helps share the load and keeps the site working if one server is down. "Non-authoritative" means the answer came
  from a DNS server that had it cached, not the domain's own official DNS server.
- **Role of DNS in a browser:** when I type a website name, the browser cannot connect to a name — it needs an IP
  address. DNS is asked first to translate the name to an IP address, and only then can the browser connect to the server.

### Task 7.3 — What happens when I open a website?
1. **I type the address** `https://example.com` in the browser and press Enter. The browser is the **client**.
2. **DNS lookup:** the browser (through the OS) asks a **DNS** server for the IP address of `example.com`. If it is not
   already cached, the DNS server finds it and replies with an address such as `172.66.147.243`.
3. **Connecting:** the client opens a connection to that IP address using the **TCP/IP protocol**, and because the
   address is `https`, it also sets up an encrypted **TLS** connection so no one in the middle can read the data.
4. **Request sent:** the browser sends an **HTTP** request (a **protocol** message) such as "GET the home page".
   The request is split into **packets** that go from my laptop to my home **router**, then through my internet
   provider's routers across the Internet towards the server.
5. **Server responds:** the web **server** receives the request, finds or builds the page, and sends back an HTTP
   response (status `200 OK` plus the HTML), again in packets.
6. **Browser builds the page:** the client puts the packets back together, reads the HTML, and requests any extra files
   it needs (CSS, images, scripts) in the same way.
7. **Page displayed:** the browser draws the finished page on my screen — the output the user sees.

## 3. Commands / tools used
| Command | Purpose |
|---------|---------|
| `ping -c 4 example.com` | Send 4 test packets to check that the website can be reached and measure the delay |
| `nslookup example.com` | Ask DNS for the IP address(es) of the domain |

## 4. My understanding
A network lets devices share data. Networks come in sizes — LAN (home), MAN (city/campus), WAN (country/world) — and the
Internet is a giant network of networks connected by routers. Every device needs an IP address, but humans use names,
so DNS translates between them. Data does not travel in one piece: it is broken into packets that follow protocols so
every device along the way knows what to do. Opening a website is a client-server conversation: my browser asks, the
server answers, and protocols like DNS, TCP/IP and HTTP(S) make it work.

## 5. Difficulties faced
- The normal `nslookup` output also showed the address of my own DNS server (my router), which is private network
  information.
- `ping` kept running when I first tried it without any options.

## 6. How I resolved them
- Removed the `Server:` and `Address: …#53` lines from the saved evidence so only the public `example.com` details remain.
- Used `ping -c 4` to send exactly 4 packets (or pressed **Ctrl + C** to stop it).

## 7. Evidence / files
- `../evidence/mission-07-network-output.txt` — `ping` and `nslookup` output (privacy-safe).
- `README.md` (this file) — concepts table and website steps.

## 8. Commit details
- Commit message: **`Explain networking concepts and website communication`**
- Pushed to GitHub and verified that the commit is visible.
