from cloudlink import cloudlink

if __name__ == "__main__":
    cl = cloudlink()

    server = cl.server(logs=True)
    server.set_motd("CL4 Optimized! Gotta Go Fast!", True)
    server.check_ip_addresses = False

    # Run the server.
    server.run(ip="0.0.0.0", port=3000)
