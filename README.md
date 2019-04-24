# UDP NAT punch-through

A proof of concept of UDP NAT punchthrough to be able to connect two peer together
without manual port forwarding on your NAT.

# Concept
Assuming two peers want to start a peer-to-peer UDP session and rendez-vous server
with a public address known by both peers.

  - Each peer first start communication with the server.
  - The server send back to each peer the public address of the other peer.
  - Thanks to first communication (peer -> server) each peer NAT has now a public endpoint
    and each peer know the other endpoint.
  - They can start sending messages to each other, it's where the NAT punch-through
    actually occurs
  - Eventually a message will reach a peer in both way, the communication is now ready


For a more detailed and accurate description, see [this link](http://bford.info/pub/net/p2pnat/)
