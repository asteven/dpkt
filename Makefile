# $Id: Makefile 345 2006-02-01 15:47:16Z dugsong $

PYTHON=	python
PKGDIR  = dpkt-`egrep version dpkt/__init__.py | cut -f2 -d"'"`
URL=	`egrep url dpkt/__init__.py | cut -f2 -d"'"`

all:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

test:
	$(PYTHON) test.py

doc:
	epydoc -o doc -n dpkt -u $(URL) --docformat=plaintext ./dpkt/

pkg_win32:
	$(PYTHON) setup.py bdist_wininst

pkg_osx:
	bdist_mpkg --readme=README --license=LICENSE
	mv dist $(PKGDIR)
	hdiutil create -srcfolder $(PKGDIR) $(PKGDIR).dmg
	mv $(PKGDIR) dist

clean:
	rm -rf build dist doc

cleandir distclean: clean
	rm -f *.pyc *~ */*.pyc */*~
