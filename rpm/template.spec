Name:           ros-kinetic-industrial-msgs
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS industrial_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/industrial_msg
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-genmsg
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-genmsg
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-trajectory-msgs

%description
The industrial message package containes industrial specific messages
definitions. This package is part of the ROS-Industrial program.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jan 16 2017 Shaun Edwards <sedwards@swri.org> - 0.6.0-0
- Autogenerated by Bloom

