#!/usr/bin/env python

import socket
import subprocess
import sys
import os.path

def main():
  envPath = ".env"
  if os.path.isfile(envPath):
    myEnv = readEnvFile(envPath)
  else:
    myEnv = {}
  
  startPortFile = "/var/run/docker_compose_start_port"
  startPort = getStartPort(startPortFile)
  services = ["NGINX_HTTP", "NGINX_HTTPS", "MYSQL", "PHPMYADMIN", "REDIS"]
  unusedPort = getUnusedPort(startPort, len(services))

  
  if len(myEnv) == 0:
    for i in range(len(services)):
      myEnv[services[i] + "_PORT"] = unusedPort[i]

    network = "_".join(unusedPort)
    try:
      subprocess.call("docker network prune -f ", shell=True)
      subprocess.call("docker network create -d bridge %s" % network, shell=True)
    except:
      pass

    myEnv["USER_NETWORK"] = network
    myEnv["WEB_ROOT"] = "../www"

    writeEnvFile(envPath, myEnv)
    setNextStartPort(startPortFile, unusedPort[-1])

  for key, value in myEnv.iteritems():
    print "%s=%s" % (key, value)

def isUsedPort(serverIP, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((serverIP, port))
  return result == 0

def getUnusedPort(start, n):
  maxPort = 65535
  if start >= maxPort:
    return []

  while(start % 100 != 0) :
    start += 1
    continue

  server = "127.0.0.1"
  serverIP = socket.gethostbyname(server)

  unused = []
  for port in range(start, start + n):
    if False == isUsedPort(serverIP, port):
      unused.append(str(port))
    else:
      return getUnusedPort(port, n)
  return unused
  
def getStartPort(path):
  if os.path.isfile(path):
    fd = open(path, "r")
    startPort = int(fd.read())
  else:
    startPort = 10000
  return startPort

def setNextStartPort(path, port):
  fd = open(path, 'w')
  fd.write(str(port))
  fd.close()
  
def writeEnvFile(path, myEnv):
  fd = open(path, 'w')
  for key, value in myEnv.iteritems():
    fd.write("%s=%s\n" % (key, value))
  fd.close()

def readEnvFile(path):
  fd = open(path, 'r')
  myEnv = {}
  for line in fd.readlines(): 
    k, v = line.split("=")
    myEnv[k.strip()] = v.strip()
  return myEnv

main()

