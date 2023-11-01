Summary:        List SCSI devices (or hosts) and associated information
Name:           lsscsi
Version:        0.32
Release:        3%{?dist}
License:        GPLv2+
Group:          Applications/System
# official git repository: https://github.com/doug-gilbert/lsscsi
Source0:        http://sg.danny.cz/scsi/%{name}-%{version}.tgz
URL:            http://sg.danny.cz/scsi/lsscsi.html
Patch0:         lsscsi-0.32-fix-uninitialized-variable.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1981038
Patch1:         lsscsi-0.33-wwn-trunc.patch

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert(at)interlog(dot)com>


%prep
%autosetup -p 1 -n %{name}-032r164

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install


%files
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Mon Aug 16 2021 Tomas Bzatek <tbzatek@redhat.com> - 0.32-3
- Fix WWN ID truncation (#1981038)

* Wed Nov 11 2020 Tomas Bzatek <tbzatek@redhat.com> - 0.32-2
- Fix an unitialized variable (Covscan)

* Tue Nov 10 2020 Tomas Bzatek <tbzatek@redhat.com> - 0.32-1
- Upgrade to 0.32 upstream snapshot (#1855766)
- Fix NVMe device parsing (#1687841, #1845977)
- Fix WWN string reporting (#1846559)
- Implement SCSI identifier sort priority (#1846566)

* Fri Aug 10 2018 Gris Ge <fge@redhat.com> 0.30-1
- Upgrade to 0.30 release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 06 2014 Dan Horák <dan[at]danny.cz> - 0.28-1
- update to 0.28

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Dan Horák <dan[at]danny.cz> - 0.27-1
- update to 0.27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> - 0.26-1
- update to 0.26

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dan Horák <dan[at]danny.cz> - 0.25-1
- update to 0.25

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  6 2010 Dan Horák <dan[at]danny.cz> - 0.23-2
- fix path separator for FC devices (#589327)
- fix for kernels with unified string representation of NULL (#589860)

* Sun Dec  6 2009 Dan Horák <dan[at]danny.cz> - 0.23-1
- update to 0.23

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Dan Horák <dan[at]danny.cz> - 0.22-1
- update to 0.22

* Tue Nov  4 2008 Dan Horák <dan[at]danny.cz> - 0.21-2
- add disttag

* Tue Nov  4 2008 Dan Horák <dan[at]danny.cz> - 0.21-1
- update to 0.21
- update urls

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.17-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-5
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.17-4
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 - Chip Coldwell <coldwell@redhat.com> 0.17-3
- bump the EVR for FC6 rebuild
* Mon Jul 17 2006 - Chip Coldwell <coldwell@redhat.com> 0.17-2
- modify spec file to meet Fedora Project packaging guidelines
* Mon Feb 06 2006 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.17-1
- fix disappearance of block device names in lk 2.6.16-rc1
* Fri Dec 30 2005 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.16-1
- wlun naming, osst and changer devices
* Tue Jul 19 2005 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.15-1
- does not use libsysfs, add filter argument, /dev scanning
* Fri Aug 20 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.13-1
- add 'timeout'
* Sun May 9 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.12-1
- rework for lk 2.6.6, device state, host name, '-d' for major+minor
* Fri Jan 09 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.11-1
- rework for lk 2.6.1
* Tue May 06 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.10-1
- adjust HBA listing for lk > 2.5.69
* Fri Apr 04 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.09-1
- fix up sorting, GPL + copyright notice
* Sun Mar 2 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.08-1
- start to add host listing support (lk >= 2.5.63)
* Fri Feb 14 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.07-1
- queue_depth name change in sysfs (lk 2.5.60)
* Mon Jan 20 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.06-1
- osst device file names fix
* Sat Jan 18 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.05-1
- output st and osst device file names (rather than "-")
* Thu Jan 14 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.04-1
- fix multiple listings of st devices (needed for lk 2.5.57)
* Thu Jan 09 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.03-1
- add --generic option (list sg devices), scsi_level output
* Wed Dec 18 2002 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.02-1
- add more options including classic mode
* Fri Dec 13 2002 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.01-1
- original
