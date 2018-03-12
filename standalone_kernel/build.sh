mkdir init
mkdir extract
cd extract
#tar -xvf ../linux-3.12.6.tar.xz 
#tar -xvf ../busybox-1.21.1.tar.bz2
####################kernel build started####################
cd linux-3.12.6
ARCH=x86_64
CROSS_COMPILE=i586-elf-
#make x86_64_defconfig
#make -j4
cd ..
####################kernel build finished##################
####################busybox build started##################
cd busybox-1.21.1
ARCH=x86
#make defconfig
echo "enable busybox setting--->build options--->build busybox as a static binary"
echo "disable networking utilities---->Support RPC services"
#make menuconfig
#make -j4 install
cd _install
find . | cpio -o --format=newc > ../../init/rootfs.img
####################busybox build finished################
cd ../../init
file rootfs.img
cd ../


####################lauch qemu############################
qemu-system-x86_64 -kernel ./linux-3.12.6/arch/x86_64/boot/bzImage -initrd ./init/rootfs.img -append "root=/dev/ram rdinit=/bin/sh"

