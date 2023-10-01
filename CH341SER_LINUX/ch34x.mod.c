#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x463acdc9, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x7b985e85, __VMLINUX_SYMBOL_STR(usb_serial_deregister_drivers) },
	{ 0xcdfddc65, __VMLINUX_SYMBOL_STR(usb_serial_register_drivers) },
	{ 0xf2b5f13f, __VMLINUX_SYMBOL_STR(kmalloc_caches) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0xab40cca9, __VMLINUX_SYMBOL_STR(__init_waitqueue_head) },
	{ 0xfe59ecff, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0xd63d6ea6, __VMLINUX_SYMBOL_STR(usb_clear_halt) },
	{ 0x4950473f, __VMLINUX_SYMBOL_STR(usb_kill_urb) },
	{ 0x9c5bc552, __VMLINUX_SYMBOL_STR(finish_wait) },
	{ 0xcb128141, __VMLINUX_SYMBOL_STR(prepare_to_wait_event) },
	{ 0x1000e51, __VMLINUX_SYMBOL_STR(schedule) },
	{ 0x622598b1, __VMLINUX_SYMBOL_STR(init_wait_entry) },
	{ 0x67b27ec1, __VMLINUX_SYMBOL_STR(tty_std_termios) },
	{ 0x569aabe6, __VMLINUX_SYMBOL_STR(tty_encode_baud_rate) },
	{ 0x409873e3, __VMLINUX_SYMBOL_STR(tty_termios_baud_rate) },
	{ 0xf2997713, __VMLINUX_SYMBOL_STR(tty_termios_hw_change) },
	{ 0xc1be4029, __VMLINUX_SYMBOL_STR(usb_control_msg) },
	{ 0x75d33bb1, __VMLINUX_SYMBOL_STR(tty_flip_buffer_push) },
	{ 0x6a1abcb, __VMLINUX_SYMBOL_STR(__tty_insert_flip_char) },
	{ 0x807b4cc0, __VMLINUX_SYMBOL_STR(tty_buffer_request_room) },
	{ 0x65345022, __VMLINUX_SYMBOL_STR(__wake_up) },
	{ 0xef7fa50f, __VMLINUX_SYMBOL_STR(__dynamic_dev_dbg) },
	{ 0xbc636bab, __VMLINUX_SYMBOL_STR(dev_err) },
	{ 0x2bcaa13, __VMLINUX_SYMBOL_STR(usb_serial_port_softint) },
	{ 0xc9e825be, __VMLINUX_SYMBOL_STR(usb_submit_urb) },
	{ 0x4829a47e, __VMLINUX_SYMBOL_STR(memcpy) },
	{ 0x97fdbab9, __VMLINUX_SYMBOL_STR(_raw_spin_unlock_irqrestore) },
	{ 0x96220280, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irqsave) },
	{ 0x1fdc7df2, __VMLINUX_SYMBOL_STR(_mcount) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";

MODULE_ALIAS("usb:v1A86p7523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p5523d*dc*dsc*dp*ic*isc*ip*in*");
