import os, re, pexpect, check50

# caesar.py
def caesar(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("caesar.py\n\n")

    # check if file exists
    if os.path.isfile(target + "/caesar.py"):
        dest.write("*PASSED* " + '-- caesar.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- caesar.py exists\n')
    totalcount += 1
    
    # encrypts 'a' as 'b' using 1 as key
    process = pexpect.spawnu('python3 {}/caesar.py 1'.format(target))
    process.expect('.*')
    process.sendline('a')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'b' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'a\' as \'b\' using 1 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'a\' as \'b\' using 1 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'barfoo' as 'yxocll' using 23 as key
    process = pexpect.spawnu('python3 {}/caesar.py 23'.format(target))
    process.expect('.*')
    process.sendline('barfoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'yxocll' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'barfoo\' as \'yxocll\' using 23 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'barfoo\' as \'yxocll\' using 23 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BARFOO' as 'EDUIRR' using 3 as key
    process = pexpect.spawnu('python3 {}/caesar.py 3'.format(target))
    process.expect('.*')
    process.sendline('BARFOO')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'EDUIRR' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BARFOO\' as \'EDUIRR\' using 3 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BARFOO\' as \'EDUIRR\' using 3 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'BaRFoo' as 'FeVJss' using 4 as key
    process = pexpect.spawnu('python3 {}/caesar.py 4'.format(target))
    process.expect('.*')
    process.sendline('BaRFoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'FeVJss' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'BaRFoo\' as \'FeVJss\' using 4 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'BaRFoo\' as \'FeVJss\' using 4 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'barfoo' as 'onesbb' using 65 as key
    process = pexpect.spawnu('python3 {}/caesar.py 65'.format(target))
    process.expect('.*')
    process.sendline('barfoo')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'onesbb' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'barfoo\' as \'onesbb\' using 65 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'barfoo\' as \'onesbb\' using 65 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # encrypts 'world, say hello!' as 'iadxp, emk tqxxa!' using 12 as key
    process = pexpect.spawnu('python3 {}/caesar.py 12'.format(target))
    process.expect('.*')
    process.sendline('world, say hello!')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = ' '.join(captured_stdout[len(captured_stdout) - 3:])
    if output != 'iadxp, emk tqxxa!' or process.isalive():
        dest.write("*FAILED* " + '-- encrypts \'world, say hello!\' as \'iadxp, emk tqxxa!\' using 12 as key\n')
    else:
        dest.write("*PASSED* " + '-- encrypts \'world, say hello!\' as \'yiadxp, emk tqxxa!\' using 12 as key\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
   
    # handles lack of argv[1]
    process = pexpect.spawnu('python3 {}/caesar.py'.format(target))
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    if process.isalive() or not process.exitstatus:
        dest.write("*FAILED* " + '-- handles lack of argv[1]\n')
    else:
        dest.write("*PASSED* " + '-- handles lack of argv[1]\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    dest.write('\ncaesar.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")

# caesar.py
def credit(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("credit.py\n\n")
    
    # check if file exists
    if os.path.isfile(target + "/credit.py"):
        dest.write("*PASSED* " + '-- credit.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- credit.py exists\n')
    totalcount += 1
    
    # input of 378282246310005 yields output of AMEX
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('378282246310005')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'AMEX' or process.isalive():
        dest.write("*FAILED* " + '-- input of 378282246310005 yields output of AMEX\n')
    else:
        dest.write("*PASSED* " + '-- input of 378282246310005 yields output of AMEX\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 371449635398431 yields output of AMEX
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('371449635398431')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'AMEX' or process.isalive():
        dest.write("*FAILED* " + '-- input of 371449635398431 yields output of AMEX\n')
    else:
        dest.write("*PASSED* " + '-- input of 371449635398431 yields output of AMEX\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 5555555555554444 yields output of MASTERCARD
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('5555555555554444')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'MASTERCARD' or process.isalive():
        dest.write("*FAILED* " + '-- input of 5555555555554444 yields output of MASTERCARD\n')
    else:
        dest.write("*PASSED* " + '-- input of 5555555555554444 yields output of MASTERCARD\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 5105105105105100 yields output of MASTERCARD
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('5105105105105100')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'MASTERCARD' or process.isalive():
        dest.write("*FAILED* " + '-- input of 5105105105105100 yields output of MASTERCARD\n')
    else:
        dest.write("*PASSED* " + '-- input of 5105105105105100 yields output of MASTERCARD\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 4111111111111111 yields output of VISA
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('4111111111111111')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'VISA' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4111111111111111 yields output of VISA\n')
    else:
        dest.write("*PASSED* " + '-- input of 4111111111111111 yields output of VISA\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 4012888888881881 yields output of VISA
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('4012888888881881')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'VISA' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4012888888881881 yields output of VISA\n')
    else:
        dest.write("*PASSED* " + '-- input of 4012888888881881 yields output of VISA\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 1234567890 yields output of INVALID
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('1234567890')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != 'INVALID' or process.isalive():
        dest.write("*FAILED* " + '-- input of 1234567890 yields output of INVALID\n')
    else:
        dest.write("*PASSED* " + '-- input of 1234567890 yields output of INVALID\n')
        passcount += 1
    totalcount += 1
    process.kill(0) 
 
    # rejects a non-numeric input of 'foo'
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'foo\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'foo\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a non-numeric input of ''
    process = pexpect.spawnu("python3 {}/credit.py".format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'foo\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'foo\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    dest.write('\ncredit.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")
    
# greedy.py
def greedy(target, dest):
    passcount, totalcount = 0, 0
    # dest.write header
    dest.write("greedy.py\n\n")

    # check if file exists
    if os.path.isfile(target + "/greedy.py"):
        dest.write("*PASSED* " + '-- greedy.py exists\n')
        passcount += 1
    else:
        dest.write("*FAILED* " + '-- greedy.py exists\n')
    totalcount += 1

    # input of 0.41 yields output of 4
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.41')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '4' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.41 yields output of 4\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.41 yields output of 4\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # input of 0.01 yields output of 1
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.01')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '1' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.01 yields output of 1\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.01 yields output of 1\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 0.15 yields output of 2
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('0.15')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '2' or process.isalive():
        dest.write("*FAILED* " + '-- input of 0.15 yields output of 2\n')
    else:
        dest.write("*PASSED* " + '-- input of 0.15 yields output of 2\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 1.6 yields output of 7
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('1.6')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '7' or process.isalive():
        dest.write("*FAILED* " + '-- input of 1.6 yields output of 7\n')
    else:
        dest.write("*PASSED* " + '-- input of 1.6 yields output of 7\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 23 yields output of 92
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('23')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '92' or process.isalive():
        dest.write("*FAILED* " + '-- input of 23 yields output of 92\n')
    else:
        dest.write("*PASSED* " + '-- input of 23 yields output of 92\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # input of 4.2 yields output of 18
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('4.2')
    process.expect([pexpect.EOF, pexpect.TIMEOUT], timeout=1)
    return_data = process.before
    captured_stdout = re.findall(r"[^(\s|\n|\r)]+", return_data)
    output = captured_stdout[len(captured_stdout) - 1]
    if output != '18' or process.isalive():
        dest.write("*FAILED* " + '-- input of 4.2 yields output of 18\n')
    else:
        dest.write("*PASSED* " + '-- input of 4.2 yields output of 18\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a negative input like -.1
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('-.1')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a negative input like -.1\n')
    else:
        dest.write("*PASSED* " + '-- rejects a negative input like -.1\n')
        passcount += 1
    totalcount += 1
    process.kill(0)
    
    # rejects a non-numeric input of 'foo'
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('foo')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'foo\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'foo\'\n')
        passcount += 1
    totalcount += 1
    process.kill(0)

    # rejects a non-numeric height of ''
    process = pexpect.spawnu("python3 {}/greedy.py".format(target))
    process.expect('.*')
    process.sendline('')
    if not process.isalive():
        dest.write("*FAILED* " + '-- rejects a non-numeric input of \'\'\n')
    else:
        dest.write("*PASSED* " + '-- rejects a non-numeric input of \'\'\n')
        passcount += 1
    totalcount += 1
        
    process.kill(0)
    dest.write('\ngreedy.py -- PASSED {} OF {} CHECKS\n'.format(passcount, totalcount))
    dest.write("\n+------------------+\n\n")