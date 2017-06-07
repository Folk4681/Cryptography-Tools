library("digest")

transaction1 = unlist(list('8eab24de5a17ba8b024d89e41d059a5ee292462604424294258b833b3db9b3c2',
                           '80b4122731e53f999a63b79bc9172d33c5cc49dfa45d791ea6ec7e0f936622c5',
                           '6fd7ff153c7fb6fdaa8c4b0dfb97af358a25b70786934dfe60051b3478c90913',
                           '284fc3bff0d49f82c9b8f51f377c42778d784b605e4aef7fe75928965b487058',
                           '7a73e3ed513e15f9ac0f7d2bf6b5c079f3ba14036ead60a5603bc7bb4863c58b',
                           '9cf185103e91c024db1024f6d73f1bc2e2f111b2453452b4ae4d42a5f3390b0d',
                           'f6a85d8a7711e5e1ba99fabdba8f580d8dddf96e985d95f73823e9799ba43663',
                           '5af7d87eb6f48a6688240ebdbae542b704253dab1602f5f57108ab4c3fee83b9'))
index = 1;
transaction2=list();
while(index<=length(transaction1)){
  hash = digest(transaction1[index], algo="sha256", serialize=FALSE);
  transaction2[index] = hash;
  index=index+1;
}


runningTimes = list();
messageLengths = list();
index = 0;
n = "q";
while(nchar(n) != 50000){
  index = index+1;
  start = Sys.time();
  hash = digest(n, algo="sha256", serialize=FALSE)
  end = Sys.time();
  RT = end - start;
  runningTimes[index] = RT
  messageLengths[index] = nchar(n)
  n = paste(n,"a",sep="");
}

messageLengths = unlist(messageLengths)
runningTimes = unlist(runningTimes)

plot(messageLengths,runningTimes,main="SHA-256 Running Time vs Message Length", xlab = "Message Length (num. of chars)", ylab = "Running Time (seconds)")

