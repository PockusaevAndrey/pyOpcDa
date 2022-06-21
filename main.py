from Structs import OPCServer

if __name__ == '__main__':
    server = OPCServer.connect("Matrikon.OPC.Simulation")

    browser = server.CreateBrowser()
    browser.ShowBranches()
