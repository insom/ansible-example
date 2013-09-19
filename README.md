Ansible Examples
================

To go along with my talk 'Python Configuration Management with Ansible', I've
created this repository for executable versions of the code featured in the
slides.

This includes some fixes to small typos, and adds an example database, models
and Flask application context to the webapp example.

The Quick Start
---------------

    pip install -r requirements.txt
    ansible-playbook -c local -i inventory simple-playbook.yml
    ansible-playbook -c local -i inventory example-lookup-playbook.yml
    python app.py
    curl http://localhost:5000/inventory/api

License
-------

Copyright (c) 2013, Aaron Brady

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
