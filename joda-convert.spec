%global pkg_name joda-convert
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.3
Release:        5.7%{?dist}
Summary:        Java library for conversion to and from standard string formats
License:        ASL 2.0 
URL:            https://github.com/JodaOrg/joda-convert/
Source0:        https://github.com/JodaOrg/joda-convert/tarball/v1.3#/joda-convert-1.3.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local

%description
Java library to enable conversion to and from standard string formats.

%package javadoc
Summary:        Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n JodaOrg-joda-convert-df6d6c9
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name}
sed -i s/// LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.3-5.7
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.3-5.6
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5.5
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5.4
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3-5
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Migrate away from mvn-rpmbuild

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue May 28 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-2
- Install NOTICE file with javadoc as well
- Use full URL for Source0

* Fri Feb 22 2013 Andy Grimm <agrimm@gmail.com> - 1.3-1
- Update to 1.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Andy Grimm <agrimm@gmail.com> - 1.2-1
- update to 1.2 and pull source tarball correctly

* Tue Oct 18 2011 Andy Grimm <agrimm@gmail.com> - 1.1-1
- Initial package
