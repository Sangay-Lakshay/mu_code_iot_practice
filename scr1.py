import scratch
s = scratch.Scratch()

s = scratch.Scratch(host='0.0.0.0', port=40000)
s.broadcast('Hello, Scratch!')