# https://leetcode.com/problems/reorder-data-in-log-files/

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs=[]
        letterLogs = []

        for log in logs:
            logArr = log.split(' ')

            identifier = logArr[0:1]
            logWoID = logArr[1:]

            # print(identifier, logWoID)

            if logWoID[0].isdigit() == True:
                identifier.extend(logWoID)
                log = ' '.join(identifier)
                digitLogs.append(log)
            else:
                logWoID.extend(identifier)
                log = ' '.join(logWoID)
                letterLogs.append(log)

        # print(digitLogs)
        letterLogs.sort()

        letterLogs2 = []

        for log in letterLogs:
            logArr = log.split(' ')
            identifier = [logArr[-1]]
            identifier.extend(logArr[:-1])
            letterLogs2.append(' '.join(identifier))

        # print(letterLogs2)

        letterLogs2.extend(digitLogs)
        return letterLogs2
