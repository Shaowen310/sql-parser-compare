from sqlparse import sql, tokens as T


class RemoveEmptyWhitespaceFilter(object):
    @staticmethod
    def _process(tlist):
        tidx = -1
        while True:
            tidx, token = tlist.token_next_by(t=T.Whitespace, idx=tidx)
            if token is None:
                break
            if token.value == '':
                tlist.tokens.remove(token)
                tidx -= 1

    def process(self, stmt):
        for sgroup in stmt.get_sublists():
            self.process(sgroup)
        RemoveEmptyWhitespaceFilter._process(stmt)
        return stmt