# QueryMind Evaluation Report

Generated on: 2026-07-23 13:25:39

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 30 |
| **Strict Passed** | 0 |
| **Partial Passed** | 0 |
| **Failed** | 30 |
| **Strict Accuracy** | **0.00%** |
| **Semantic / Partial Match Accuracy** | **0.00%** |
| **Average Latency** | 4.07s |

## Difficulty Breakdown

| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| --- | --- | --- | --- | --- |
| Simple | 10 | 0 | 0 | 0.00% |
| Medium | 10 | 0 | 0 | 0.00% |
| Hard | 10 | 0 | 0 | 0.00% |

## Failure Analysis Details

### Failure / Projection Categorization Breakdown

| Category | Count |
| --- | --- |
| **Execution** | 30 |

---

### Test ID 1 (Simple) - [FAIL]
**Question:** `List the Name of all artists ordered alphabetically.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EAA0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093EAA0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EAA0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EAA0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name FROM Artist ORDER BY Name ASC;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 275 | **Actual Row Count:** 0

---

### Test ID 2 (Simple) - [FAIL]
**Question:** `Show the Title of the top 5 longest tracks.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F4F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F4F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F4F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F4F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name FROM Track ORDER BY Milliseconds DESC LIMIT 5;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 5 | **Actual Row Count:** 0

---

### Test ID 3 (Simple) - [FAIL]
**Question:** `List all distinct genres.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EBF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093EBF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EBF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EBF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT DISTINCT Name FROM Genre;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 25 | **Actual Row Count:** 0

---

### Test ID 4 (Simple) - [FAIL]
**Question:** `Show the FirstName and LastName of all customers from Brazil.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093FBB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093FBB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093FBB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093FBB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT FirstName, LastName FROM Customer WHERE Country = 'Brazil';
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 5 | **Actual Row Count:** 0

---

### Test ID 5 (Simple) - [FAIL]
**Question:** `List the names of all playlists.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04370>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30A04370>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04370>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04370>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name FROM Playlist;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 18 | **Actual Row Count:** 0

---

### Test ID 6 (Simple) - [FAIL]
**Question:** `Find the email address of customer named Luís Gonçalves.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04AF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30A04AF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04AF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A04AF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Email FROM Customer WHERE FirstName = 'Luís' AND LastName = 'Gonçalves';
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 7 (Simple) - [FAIL]
**Question:** `Show the names of all media types.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F820>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F820>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F820>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F820>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name FROM MediaType;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 5 | **Actual Row Count:** 0

---

### Test ID 8 (Simple) - [FAIL]
**Question:** `List the top 10 most expensive tracks.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093DF30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093DF30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093DF30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093DF30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name, UnitPrice FROM Track ORDER BY UnitPrice DESC LIMIT 10;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 10 | **Actual Row Count:** 0

---

### Test ID 9 (Simple) - [FAIL]
**Question:** `Show all employees ordered by their HireDate.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EE30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093EE30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EE30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EE30>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT FirstName, LastName, HireDate FROM Employee ORDER BY HireDate ASC;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 8 | **Actual Row Count:** 0

---

### Test ID 10 (Simple) - [FAIL]
**Question:** `List the names of tracks longer than 5 minutes.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1C3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30A1C3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1C3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1C3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Name FROM Track WHERE Milliseconds > 300000;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1069 | **Actual Row Count:** 0

---

### Test ID 11 (Medium) - [FAIL]
**Question:** `Show the Title of albums created by the artist AC/DC.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BCD0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30A1BCD0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BCD0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BCD0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Album.Title FROM Album JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Artist.Name = 'AC/DC';
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 2 | **Actual Row Count:** 0

---

### Test ID 12 (Medium) - [FAIL]
**Question:** `List the Name of tracks and their genre.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAC3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30AAC3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAC3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAC3A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Track.Name, Genre.Name FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 3503 | **Actual Row Count:** 0

---

### Test ID 13 (Medium) - [FAIL]
**Question:** `Find the customers who have placed invoices worth more than $10.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AACB20>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30AACB20>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AACB20>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AACB20>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId WHERE i.Total > 10;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 59 | **Actual Row Count:** 0

---

### Test ID 14 (Medium) - [FAIL]
**Question:** `Show all tracks that belong to the Rock genre.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAFD60>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30AAFD60>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAFD60>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AAFD60>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Track.Name FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId WHERE Genre.Name = 'Rock';
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1297 | **Actual Row Count:** 0

---

### Test ID 15 (Medium) - [FAIL]
**Question:** `List customer names and the total amount they spent.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BF70>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30A1BF70>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BF70>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30A1BF70>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId, c.FirstName, c.LastName;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 59 | **Actual Row Count:** 0

---

### Test ID 16 (Medium) - [FAIL]
**Question:** `Find all tracks in the playlist named Music.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AE50F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA30AE50F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AE50F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA30AE50F0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Track.Name FROM Track JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId JOIN Playlist ON PlaylistTrack.PlaylistId = Playlist.PlaylistId WHERE Playlist.Name = 'Music';
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 6580 | **Actual Row Count:** 0

---

### Test ID 17 (Medium) - [FAIL]
**Question:** `Show the employee and the customers assigned to them.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C6A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093C6A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C6A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C6A0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT e.FirstName, e.LastName, c.FirstName, c.LastName FROM Employee e JOIN Customer c ON e.EmployeeId = c.SupportRepId;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 59 | **Actual Row Count:** 0

---

### Test ID 18 (Medium) - [FAIL]
**Question:** `List the artists and the number of albums they have.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CEB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093CEB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CEB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CEB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Artist.Name, COUNT(Album.AlbumId) AS AlbumCount FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId GROUP BY Artist.ArtistId, Artist.Name;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 204 | **Actual Row Count:** 0

---

### Test ID 19 (Medium) - [FAIL]
**Question:** `Find the countries with more than 5 customers.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D630>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093D630>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D630>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D630>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Country FROM Customer GROUP BY Country HAVING COUNT(CustomerId) > 5;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 2 | **Actual Row Count:** 0

---

### Test ID 20 (Medium) - [FAIL]
**Question:** `Show the names of albums that contain more than 10 tracks.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F070>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F070>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F070>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F070>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Album.Title FROM Album JOIN Track ON Album.AlbumId = Track.AlbumId GROUP BY Album.AlbumId, Album.Title HAVING COUNT(Track.TrackId) > 10;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 183 | **Actual Row Count:** 0

---

### Test ID 21 (Hard) - [FAIL]
**Question:** `Find the top 5 customers by total spending.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CD90>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093CD90>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CD90>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CD90>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId, c.FirstName, c.LastName ORDER BY TotalSpent DESC LIMIT 5;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 5 | **Actual Row Count:** 0

---

### Test ID 22 (Hard) - [FAIL]
**Question:** `Show the artist whose tracks generated the highest revenue.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C880>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093C880>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C880>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C880>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Artist.Name, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS Revenue FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId JOIN Track ON Album.AlbumId = Track.AlbumId JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.ArtistId, Artist.Name ORDER BY Revenue DESC LIMIT 1;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 23 (Hard) - [FAIL]
**Question:** `Find the genre with the highest number of purchases.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C0D0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093C0D0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C0D0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C0D0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Genre.Name, SUM(InvoiceLine.Quantity) AS TotalPurchased FROM Genre JOIN Track ON Genre.GenreId = Track.GenreId JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Genre.GenreId, Genre.Name ORDER BY TotalPurchased DESC LIMIT 1;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 24 (Hard) - [FAIL]
**Question:** `List customers who purchased tracks from more than 3 different genres.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F580>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F580>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F580>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F580>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT c.FirstName, c.LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId JOIN Track t ON il.TrackId = t.TrackId GROUP BY c.CustomerId, c.FirstName, c.LastName HAVING COUNT(DISTINCT t.GenreId) > 3;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 59 | **Actual Row Count:** 0

---

### Test ID 25 (Hard) - [FAIL]
**Question:** `Find the total sales amount for each year.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EEF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093EEF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EEF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093EEF0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT strftime('%Y', InvoiceDate) AS SalesYear, SUM(Total) AS TotalSales FROM Invoice GROUP BY SalesYear;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 5 | **Actual Row Count:** 0

---

### Test ID 26 (Hard) - [FAIL]
**Question:** `Show the most purchased track.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C700>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093C700>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C700>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093C700>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Track.Name, SUM(InvoiceLine.Quantity) AS TotalPurchased FROM Track JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Track.TrackId, Track.Name ORDER BY TotalPurchased DESC LIMIT 1;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 27 (Hard) - [FAIL]
**Question:** `Find the average track price for each genre.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CB50>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093CB50>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CB50>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093CB50>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Genre.Name, AVG(Track.UnitPrice) AS AvgPrice FROM Genre JOIN Track ON Genre.GenreId = Track.GenreId GROUP BY Genre.GenreId, Genre.Name;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 25 | **Actual Row Count:** 0

---

### Test ID 28 (Hard) - [FAIL]
**Question:** `List artists that have tracks in more than 2 playlists.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D180>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093D180>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D180>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093D180>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Artist.Name FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId JOIN Track ON Album.AlbumId = Track.AlbumId JOIN PlaylistTrack ON Track.TrackId = PlaylistTrack.TrackId GROUP BY Artist.ArtistId, Artist.Name HAVING COUNT(DISTINCT PlaylistTrack.PlaylistId) > 2;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 152 | **Actual Row Count:** 0

---

### Test ID 29 (Hard) - [FAIL]
**Question:** `Show the country that generated the highest revenue.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT BillingCountry, SUM(Total) AS TotalRevenue FROM Invoice GROUP BY BillingCountry ORDER BY TotalRevenue DESC LIMIT 1;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 30 (Hard) - [FAIL]
**Question:** `Find customers who never made a purchase.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Pipeline crashed: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 95, in create_connection
    raise err
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 239, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 969, in send
    self.connect()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 205, in connect
    conn = self._new_conn()
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\urllib3\util\retry.py", line 592, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\Shrikar\PR\QueryMind\backend\evaluation_runner.py", line 169, in main
    pipeline_result = run_querymind(question, connector)
  File "E:\Shrikar\PR\QueryMind\backend\pipeline\querymind_pipeline.py", line 280, in run_querymind
    query_plan_raw = plan_query(query, formatted_schema, column_mapping)
  File "E:\Shrikar\PR\QueryMind\backend\llm\llm_planner.py", line 163, in plan_query
    response = requests.post(
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\Developmrnt Team\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\adapters.py", line 565, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=11434): Max retries exceeded with url: /api/generate (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CA3093F280>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))
*

**Expected SQL:**
```sql
SELECT Customer.FirstName, Customer.LastName FROM Customer LEFT JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId WHERE Invoice.InvoiceId IS NULL;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 0 | **Actual Row Count:** 0

---

